# En Online Chat-applikation skapad med Flask och Flask-SocketIO

## Översikt
Detta är en online chat-applikation byggd med hjälp av Flask och Flask-SocketIO. Applikationen gör det möjligt för flera användare att gå med i egna chattrum och kommunicera i realtid.

## Bibliotek och Verktyg
För att utveckla denna chat-applikation användes följande bibliotek och verktyg:

### Bibliotek

- **Flask**
  - **Beskrivning:** Flask är ett lättviktigt ramverk för att bygga webbtjänster i Python. Det används för att hantera webbservern och routing i applikationen.
  - **Installation:**
    ```bash
    pip install Flask
    ```

- **Flask-SocketIO**
  - **Beskrivning:** Flask-SocketIO möjliggör WebSocket-kommunikation i Flask-applikationer. Det används för att hantera realtidskommunikation mellan klienter och server.
  - **Installation:**
    ```bash
    pip install Flask-SocketIO
    ```
    
## Instruktioner

1. **Klona repot:**
    ```bash
    git clone https://github.com/strandafredde/Online-Chat-App
    cd online-chat-app
    ```

2. **Skapa en virtuell miljö** (valfritt men rekommenderat):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # På Windows använd `venv\Scripts\activate`
    ```

3. **Installera de nödvändiga paketen:**
    ```bash
    pip install Flask-SocketIO
    pip install Flask
    ```

4. **Kör applikationen:**
    ```bash
    python main.py
    ```

5. **Gå till applikationen:**
    Öppna din webbläsare och navigera till `http://127.0.0.1:5000/` för att komma åt chattapplikationen.
