"""Karaoke — локальное караоке-приложение.

Запуск:  python main.py   (или run.bat на Windows)
"""
import os
import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow
from app.ui.theme import STYLESHEET


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = QApplication(sys.argv)
    app.setApplicationName("Karaoke")
    app.setStyleSheet(STYLESHEET)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
