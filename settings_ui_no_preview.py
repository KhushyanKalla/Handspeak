from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QSpacerItem, QSizePolicy,
)
from PyQt5.QtGui import QFont, QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt, QSize
import sys

class SettingsUINoPreview(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
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
        self.set_background()
        super().resizeEvent(event)

    def initUI(self):
        main_layout = QVBoxLayout(self)

        # Header
        header_layout = QHBoxLayout()

        header_icon = QLabel()
        header_icon.setPixmap(QIcon("header_icon.png").pixmap(40, 40))
        header_layout.addWidget(header_icon, alignment=Qt.AlignLeft)

        header = QLabel("HANDSPEAK - SETTINGS")
        header.setFont(QFont("Arial", 30, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header)

        header_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(header_layout)
        main_layout.addSpacing(30)

        # Main Body Layout
        body_layout = QHBoxLayout()

        # Left Menu
        menu_layout = QVBoxLayout()
        menu_layout.setAlignment(Qt.AlignCenter)
        menu_layout.setSpacing(15)

        def menu_button(text, color):
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
            btn.setCursor(Qt.PointingHandCursor)
            return btn

        theme_btn = menu_button("THEME", "#00FF7F")
        camera_btn = menu_button("CAMERA SOURCE", "#FF6347")
        text_to_speech_btn = menu_button("TEXT TO SPEECH", "#FF6347")
        report_issue_btn = menu_button("REPORT AN ISSUE", "#FF6347")

        menu_layout.addWidget(theme_btn)
        menu_layout.addWidget(camera_btn)
        menu_layout.addWidget(text_to_speech_btn)
        menu_layout.addWidget(report_issue_btn)

        # Spacer
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        body_layout.addLayout(menu_layout)

        main_layout.addLayout(body_layout)

        main_layout.addSpacing(30)

        # Quote
        quote = QLabel("“Breaking Barriers, One Sign at a Time”")
        quote.setStyleSheet("color: red; font-style: italic;")
        quote.setFont(QFont("Arial", 12))
        quote.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(quote)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsUINoPreview()
    window.show()
    sys.exit(app.exec_())
