import os
import sys
from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QFont, QFontMetrics, QPaintEvent, QColor, Qt


class MyRibbon(QWidget):
    def __init__(self):
        super().__init__()

        self.test_text="this is a demo text to show if the project works"
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_text_position)
        self.timer.start(16)
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.font = QFont("Ubuntu", 14)
        self.font.setBold(True)
        self.metrics = QFontMetrics(self.font)
        self.text_width=self.metrics.horizontalAdvance(self.test_text)

        self.screen_geo=QApplication.primaryScreen().availableGeometry()
        self.x_location=self.screen_geo.width()
        self.window_height=40
        self.setGeometry(0,self.screen_geo.height(),self.screen_geo.width(),self.window_height)
    def update_text_position(self):
        self.x_location -= 2
        if self.x_location < -(self.text_width):
            self.x_location = self.screen_geo.width()

        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QColor("White"))
        painter.fillRect(self.rect(), QColor("Blue"))
        painter.setFont(self.font)
        y=(self.metrics.ascent()+self.window_height//2-(self.metrics.ascent()//2))
        painter.drawText(self.x_location,y, self.test_text)

    def mousePressEvent(self, event):
        print("mousePressEvent")
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_pos)

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
if __name__ == '__main__':
    if sys.platform.startswith("linux"):
        if os.environ.get("XDG_SESSION_TYPE") == "wayland":
            os.environ["QT_QPA_PLATFORM"] = "xcb"
    app = QApplication(sys.argv)

    window = MyRibbon()
    window.show()
    sys.exit(app.exec())
