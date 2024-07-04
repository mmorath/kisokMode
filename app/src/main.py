#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Module: Web Display
Description:
    Dieses Modul zeigt eine oder mehrere dynamische Webseiten auf einem großen Monitor an und
    aktualisiert diese regelmäßig. Es kann mit Konfigurationsargumenten oder einer
    Konfigurationsdatei betrieben werden. Logging wird für die Überwachung und
    Fehlerverfolgung verwendet.

Author: Ihr Name
Creation Date: 2024-07-04
Version: 1.0.0
License: MIT

Dependencies:
    - webbrowser: Für das Öffnen der Webseite im Browser
    - time: Für die Implementierung des Aktualisierungsintervalls
    - os: Für das Steuern des Browsers über das Betriebssystem
    - logging: Für die Protokollierung der Aktivitäten
    - json: Für das Laden der Konfigurationsdatei
    - argparse: Für die Handhabung von Befehlszeilenargumenten
    - keyboard: Für das Überwachen von Tastendrücken

Usage:
    Starten Sie das Skript mit folgenden Befehlen:

    1. Mit einer spezifischen Webseite und einem Aktualisierungsintervall:
       python3 src/main.py --url http://tagesschau.de --interval 60

    2. Mit einer Konfigurationsdatei:
       python3 src/main.py --config config/config.json

    3. Ohne zusätzliche Argumente (es wird die Standard-Konfigurationsdatei verwendet):
       python3 src/main.py
"""

import webbrowser
import time
import os
import logging
import json
import argparse
import keyboard  # Importiert die keyboard-Bibliothek für das Überwachen von Tastendrücken
import logging_config  # Importiert die Logging-Konfiguration

def load_config(config_path):
    """
    Lädt die Konfigurationsdatei.

    Args:
        config_path (str): Pfad zur Konfigurationsdatei.

    Returns:
        dict: Konfigurationsparameter.
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def open_browser(url):
    """
    Öffnet die angegebene URL im Chromium-Browser im Kiosk-Modus.

    Args:
        url (str): Die URL der Webseite, die geöffnet werden soll.
    """
    logging.info(f"Öffne URL: {url}")
    os.system(f'chromium-browser --kiosk --start-fullscreen {url}')

def refresh_browser(interval, urls):
    """
    Aktualisiert die angegebenen URLs im Chromium-Browser in regelmäßigen Abständen.

    Args:
        interval (int): Das Aktualisierungsintervall in Sekunden.
        urls (list): Die URLs der Webseiten, die aktualisiert werden sollen.
    """
    while True:
        for url in urls:
            if keyboard.is_pressed('ctrl+q'):
                logging.info("Programm beendet durch Benutzer")
                os.system('pkill chromium-browser')
                exit()
            logging.info(f"Zeige URL: {url}")
            os.system('pkill chromium-browser')
            open_browser(url)
            for _ in range(interval):
                time.sleep(1)
                if keyboard.is_pressed('ctrl+q'):
                    logging.info("Programm beendet durch Benutzer")
                    os.system('pkill chromium-browser')
                    exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Display Project')
    parser.add_argument('--config', type=str, default='../config/config.json', help='Pfad zur Konfigurationsdatei')
    parser.add_argument('--url', type=str, help='Die URL der Webseite, die angezeigt werden soll')
    parser.add_argument('--interval', type=int, help='Das Aktualisierungsintervall in Sekunden')
    args = parser.parse_args()

    config = load_config(args.config)

    if args.url:
        URLS = [args.url]
    else:
        URLS = config.get("urls") if "urls" in config else [config.get("url")]

    REFRESH_INTERVAL = args.interval if args.interval else config.get("refresh_interval")

    logging.info("Starte Web-Display Service")
    try:
        refresh_browser(REFRESH_INTERVAL, URLS)
    except Exception as e:
        logging.error(f"Fehler im Web-Display Service: {e}")
