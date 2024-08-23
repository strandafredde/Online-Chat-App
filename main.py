import random
import string
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


rooms = {}
#======================================= FUNCTIONS  =======================================
def generate_room_id(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(string.ascii_letters)
        if code not in rooms:
            break
    return code


@socketio.on('connect')
def on_join(auth):
    room = session.get('room')
    nickname = session.get('nickname')
    if room is None or nickname is None:
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    send({'name': nickname, 'msg': 'has joined the room.'}, room=room)
    rooms[room]['member'] += 1
    print(nickname + f" has joined the room: {room}.")

    
@socketio.on('disconnect')
def on_leave():
    room = session.get('room')
    nickname = session.get('nickname')
    leave_room(room)
    if room in rooms:
        rooms[room]['member'] -= 1
        if rooms[room]['member'] == 0:
            del rooms[room]
    send({'name': nickname, 'msg': 'has left the room.'}, room=room)
    print(nickname + f" has left the room: {room}.")

@socketio.on('message')
def on_message(data):
    room = session.get('room')
    nickname = session.get('nickname')
    if room is None or nickname is None:
        return
    content = {
        'name': nickname,
        'msg': data['msg']
    }
    send(content, to=room)
    rooms[room]['messages'].append(content)
    print(nickname + f" has sent a message: {data['msg']}.")


#======================================= ROUTES  =======================================
@app.route('/', methods=['GET', 'POST'])
def home():
    session.clear()
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        room_id = request.form.get('room_id')
        create = request.form.get('create', False)
        join = request.form.get('join', False)
        print(nickname)
        print(create)
        print(join)

        if not nickname:
            return render_template('homepage.html', error='Nickname is required', room_id=room_id, nickname=nickname)
        
        if join != False and not room_id:
            return render_template('homepage.html', error='Please select either create or join', room_id=room_id, nickname=nickname)
        
        room = room_id
        if create != False:
            room = generate_room_id(4)
            rooms[room] = {'member': 0, 'messages': []}
        
        elif room_id not in rooms:
            return render_template('homepage.html', error='Room does not exist', room_id=room_id, nickname=nickname)

        session['room'] = room
        session['nickname'] = nickname
        return redirect(url_for('room'))
    
    return render_template('homepage.html')



@app.route('/room' , methods=['GET', 'POST'])
def room():
    room = session.get('room')
    nickname = session.get('nickname')
    if room is None or nickname is None or room not in rooms:
        return redirect(url_for('home'))
    return render_template('room.html' , room=room, nickname=nickname, messages=rooms[room]['messages'])


if __name__ == '__main__':
   socketio.run(app, host='0.0.0.0', port=5000, debug=True)