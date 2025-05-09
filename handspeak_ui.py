from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QFrame, QSpacerItem, QSizePolicy,
)
from PyQt5.QtGui import QFont, QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt, QSize
import sys
import subprocess

class HandspeakUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HANDSPEAK")
        self.setGeometry(100, 100, 900, 600)
        self.set_background()
        self.initUI()

    def set_background(self):
        # Set the background image to be responsive
        background = QPixmap("ASL hand recognition/src/BG2.png")
        background = background.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

    def resizeEvent(self, event):
        # Ensure the background image resizes properly when the window size changes
        self.set_background()
        super().resizeEvent(event)

    def initUI(self):
        main_layout = QVBoxLayout(self)

        # ===== Header with Title and Icon on Left =====
        header_layout = QHBoxLayout()

        # Add icon to the left of the header (change to your icon file path)
        header_icon = QLabel()
        header_icon.setPixmap(QIcon("header_icon.png").pixmap(40, 40))
        header_layout.addWidget(header_icon, alignment=Qt.AlignLeft)

        # Title text
        header = QLabel("HANDSPEAK")
        header.setFont(QFont("Arial", 30, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header)

        header_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(header_layout)

        # ===== Add space between header and body =====
        main_layout.addSpacing(30)

        # ===== Main Body Layout =====
        body_layout = QHBoxLayout()

        # ------ Left Menu ------ (same as before)
        menu_layout = QVBoxLayout()
        menu_layout.setAlignment(Qt.AlignCenter)
        menu_layout.setSpacing(15)

        def menu_button(icon_path, text, color):
            btn = QPushButton(f"  {text}")
            btn.setFont(QFont("Segoe UI", 13, QFont.Bold))
            btn.setStyleSheet(f"""
                QPushButton {{
                    color: {color};
                    background-color: rgba(255, 255, 255, 0.05);
                    border: 2px solid {color};
                    border-radius: 8px;
                    padding: 10px 15px;
                    text-align: left;
                }}
                QPushButton:hover {{
                    background-color: rgba(255, 255, 255, 0.15);
                }}
                QPushButton:pressed {{
                    background-color: rgba(255, 255, 255, 0.25);
                }}
            """)
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(30, 30))
            btn.setCursor(Qt.PointingHandCursor)
            return btn

        # Create buttons (same as before)
        start_btn = menu_button("start.png", "START COMMUNICATION", "#00FF7F")
        history_btn = menu_button("history.png", "HISTORY", "#FF6347")
        manual_btn = menu_button("manual.png", "USER MANUAL", "#FF6347")
        settings_btn = menu_button("settings.png", "SETTINGS", "#FF6347")
        about_btn = menu_button("about.png", "ABOUT", "#FF6347")

        # Connect Start button (same as before)
        start_btn.clicked.connect(self.start_communication)

        # Add buttons to the menu layout
        menu_layout.addWidget(start_btn)
        menu_layout.addWidget(history_btn)
        menu_layout.addWidget(manual_btn)
        menu_layout.addWidget(settings_btn)
        menu_layout.addWidget(about_btn)

        # ===== Add space between the menu and live preview =====
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ------ Live Preview Box ------ (no camera feed now)
        preview_frame = QFrame()
        preview_frame.setStyleSheet("background-color: rgba(0, 0, 0, 0.7); border-radius: 12px;")
        preview_frame.setMinimumSize(350, 350)

        preview_layout = QVBoxLayout(preview_frame)
        preview_label = QLabel("LIVE PREVIEW")
        preview_label.setStyleSheet("color: white;")
        preview_label.setFont(QFont("Arial", 14))
        preview_label.setAlignment(Qt.AlignCenter)
        preview_layout.addWidget(preview_label)

        # Add menu and preview to main body
        body_layout.addLayout(menu_layout)
        body_layout.addWidget(preview_frame)
        main_layout.addLayout(body_layout)

        # ===== Add space between preview and quote =====
        main_layout.addSpacing(30)

        # ===== Quote =====
        quote = QLabel("“Breaking Barriers, One Sign at a Time”")
        quote.setStyleSheet("color: red; font-style: italic;")
        quote.setFont(QFont("Arial", 12))
        quote.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(quote)

    def start_communication(self):
        script_path = r"C:\Users\khush\Sem 6\HandSpeak\ASL hand recognition\src\real_time_recognition.py"
        try:
            subprocess.Popen(["python", script_path], shell=True)
        except Exception as e:
            print(f"Error occurred while starting the communication: {e}")
            
    def open_settings(self):
        from settings_ui import SettingsUI  # or from settings_ui_no_preview import SettingsUINoPreview
        settings_window = SettingsUI(with_live_preview=True)  # or SettingsUINoPreview
        settings_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandspeakUI()
    window.show()
    sys.exit(app.exec_())
