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
        background = QPixmap("ASL hand recognition/src/BG2.png")
        background = background.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(palette)

    def resizeEvent(self, event):
        # Ensure the background image resizes properly when the window size changes
        self.set_background()
        super().resizeEvent(event)
        self.adjust_button_size()

    def adjust_button_size(self):
        # Increase button size when the window is maximized (full screen)
        if self.isMaximized():
            button_size = 18  # Larger font size
        else:
            button_size = 13  # Regular font size
        
        for btn in self.findChildren(QPushButton):
            btn.setFont(QFont("Segoe UI", button_size, QFont.Bold))

    def initUI(self):
        main_layout = QVBoxLayout(self)

        # ===== Header with Title and Icon on Left =====
        header_layout = QHBoxLayout()

        header_icon = QLabel()
        header_icon.setPixmap(QIcon("header_icon.png").pixmap(40, 40))
        header_layout.addWidget(header_icon, alignment=Qt.AlignLeft)

        header = QLabel("HANDSPEAK")
        header.setFont(QFont("Arial", 30, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header)

        header_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(header_layout)

        main_layout.addSpacing(30)

        # ===== Main Body Layout (without Live Preview) =====
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
                    background-color: rgba(255, 255, 255, 0.2);
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

        # ===== Add Spacer to Adjust Space Between Buttons =====
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Add menu to body layout (removed the preview section)
        body_layout.addLayout(menu_layout)

        main_layout.addLayout(body_layout)

        # ===== Add space between the menu and quote =====
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandspeakUI()
    window.show()
    sys.exit(app.exec_())
