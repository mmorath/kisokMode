#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Module: Web Display with PyQt5
Description:
    Dieses Modul zeigt eine oder mehrere dynamische Webseiten auf einem großen Monitor an und
    aktualisiert diese regelmäßig mit PyQt5.

Author: Ihr Name
Creation Date: 2024-07-04
Version: 1.0.0
License: MIT

Dependencies:
    - PyQt5: Für das Anzeigen der Webseite

Usage:
    Starten Sie das Skript mit folgenden Befehlen:

    1. Mit einer spezifischen Webseite und einem Aktualisierungsintervall:
       python3 app/src/main.py --url http://tagesschau.de --interval 60

    2. Mit einer Konfigurationsdatei:
       python3 app/src/main.py --config app/config/config.json

    3. Ohne zusätzliche Argumente (es wird die Standard-Konfigurationsdatei verwendet):
       python3 app/src/main.py
"""

import sys
import json
import argparse
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QShortcut
from PyQt5.QtCore import QUrl, QTimer, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QKeySequence
import os

# Pfad zum Verzeichnis "app" hinzufügen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

import logging_config  # Importiert die Logging-Konfiguration

class WebDisplay(QMainWindow):
    def __init__(self, urls, interval):
        super().__init__()
        self.urls = urls
        self.interval = interval
        self.current_url_index = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Display')
        self.setGeometry(0, 0, 1920, 1080)  # Vollbildauflösung

        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(self.web_view.settings().WebAttribute.FullScreenSupportEnabled, True)
        self.web_view.settings().setAttribute(self.web_view.settings().WebAttribute.PluginsEnabled, True)
        self.web_view.settings().setAttribute(self.web_view.settings().WebAttribute.JavascriptEnabled, True)
        self.web_view.settings().setAttribute(self.web_view.settings().WebAttribute.AutoLoadImages, True)
        self.web_view.page().profile().setHttpUserAgent(
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        )
        self.web_view.setUrl(QUrl(self.urls[self.current_url_index]))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_browser)
        self.timer.start(self.interval * 1000)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.web_view)

        self.showFullScreen()

        # Tastenkombination für das Beenden der Anwendung hinzufügen
        quit_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)
        quit_shortcut.activated.connect(self.close_application)

    def refresh_browser(self):
        self.current_url_index = (self.current_url_index + 1) % len(self.urls)
        logging.info(f"Zeige URL: {self.urls[self.current_url_index]}")
        self.web_view.setUrl(QUrl(self.urls[self.current_url_index]))

    def close_application(self):
        logging.info("Programm beendet durch Benutzer")
        self.timer.stop()
        self.web_view.stop()
        self.close()

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Display Project with PyQt5')
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

    app = QApplication(sys.argv)
    ex = WebDisplay(URLS, REFRESH_INTERVAL)
    sys.exit(app.exec_())
