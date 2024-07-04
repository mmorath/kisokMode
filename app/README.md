# KIOSKMODE Project

Dieses Projekt zeigt eine oder mehrere dynamische Webseiten auf einem großen Monitor an und aktualisiert diese regelmäßig.

## Installation und Ausführung

### Voraussetzungen

- Raspberry Pi mit Raspbian installiert
- Chromium-Browser

### Schritte

1. Klonen Sie das Projekt:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Führen Sie das Setup-Skript aus, um die Umgebung vorzubereiten:
    ```bash
    ./installEnv.sh
    ```

3. Passen Sie die Konfigurationsdatei `config/config.json` an:
    ```json
    {
        "urls": [
            "http://example.com",
            "http://tagesschau.de"
        ],
        "refresh_interval": 300
    }
    ```

4. Starten Sie das Skript:
    ```bash
    python3 src/main.py --config config/config.json
    ```

### Beispiel

1. Mit einer spezifischen Webseite und einem Aktualisierungsintervall:
    ```bash
    python3 src/main.py --url http://tagesschau.de --interval 60
    ```

2. Mit einer Konfigurationsdatei:
    ```bash
    python3 src/main.py --config config/config.json
    ```

3. Ohne zusätzliche Argumente (es wird die Standard-Konfigurationsdatei verwendet):
    ```bash
    python3 src/main.py
    ```

### Automatischer Start bei Hochfahren

Fügen Sie folgende Zeile zur Datei `/etc/rc.local` hinzu, um das Skript beim Hochfahren automatisch zu starten:

```bash
python3 /path/to/your/project/src/main.py --config /path/to/your/project/config/config.json &
```

### Beenden des Programms

Drücken Sie `Ctrl + Q`, um das Programm zu beenden und den Chromium-Browser zu schließen.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.
```