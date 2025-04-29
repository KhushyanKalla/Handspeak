from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QFrame, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
import sys
import subprocess  # 🔥 Added to run real_time_recognition.py

class HandspeakUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HANDSPEAK")
        self.setGeometry(100, 100, 900, 600)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)

        # ===== Header with Title and Icon on Left =====
        header_layout = QHBoxLayout()
        
        # Add icon to the left of the header (change to your icon file path)
        header_icon = QLabel()
        header_icon.setPixmap(QIcon("header_icon.png").pixmap(40, 40))  # Adjust the size of the icon
        header_layout.addWidget(header_icon, alignment=Qt.AlignLeft)

        # Title text
        header = QLabel("HANDSPEAK")
        header.setFont(QFont("Arial", 30, QFont.Bold))  # Increased font size
        header.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header)
        
        header_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(header_layout)

        # ===== Add space between header and body =====
        main_layout.addSpacing(30)  # Increased space after the header

        # ===== Main Body Layout =====
        body_layout = QHBoxLayout()

        # ------ Left Menu ------ 
        menu_layout = QVBoxLayout()
        menu_layout.setAlignment(Qt.AlignCenter)  # Align buttons to the center
        menu_layout.setSpacing(15)  # Increased spacing between buttons

        def menu_button(icon_path, text, color):
            btn = QPushButton(f"  {text}")
            btn.setFont(QFont("Arial", 14, QFont.Bold))  # Increased font size
            btn.setStyleSheet(f"color: {color}; text-align: left; border: none;")
            btn.setIcon(QIcon(icon_path))  
            btn.setIconSize(QSize(30, 30))  # Increased icon size
            btn.setCursor(Qt.PointingHandCursor)
            return btn

        # Create buttons
        start_btn = menu_button("start.png", "START COMMUNICATION", "green")
        history_btn = menu_button("history.png", "HISTORY", "red")
        manual_btn = menu_button("manual.png", "USER MANUAL", "red")
        settings_btn = menu_button("settings.png", "SETTINGS", "red")
        about_btn = menu_button("about.png", "ABOUT", "red")

        # Connect Start button to open real_time_recognition.py
        start_btn.clicked.connect(self.start_communication)

        # Add buttons to the menu layout
        menu_layout.addWidget(start_btn)
        menu_layout.addWidget(history_btn)
        menu_layout.addWidget(manual_btn)
        menu_layout.addWidget(settings_btn)
        menu_layout.addWidget(about_btn)

        # ===== Add space between the menu and live preview =====
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ------ Live Preview Box ------ 
        preview_frame = QFrame()
        preview_frame.setStyleSheet("background-color: black;")
        preview_frame.setMinimumSize(350, 350)

        preview_layout = QVBoxLayout(preview_frame)
        preview_label = QLabel("LIVE PREVIEW")
        preview_label.setStyleSheet("color: white;")
        preview_label.setFont(QFont("Arial", 14))  # Increased font size for preview label
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

        # ===== Removed Accept Button =====

    def start_communication(self):
        # 🔥 Open real_time_recognition.py
        subprocess.Popen(["python", r"C:\Users\khush\Sem 6\HandSpeak\ASL hand recognition\src\real_time_recognition.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandspeakUI()
    window.show()
    sys.exit(app.exec_())
