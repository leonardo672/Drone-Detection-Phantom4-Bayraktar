import sys
import os
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QFileDialog, QApplication
)
from PyQt5.QtGui import QPixmap, QFont, QBrush, QPalette
from PyQt5.QtCore import Qt

from gui.image_display_form import ImageDisplayForm
from gui.images_child_form import ImagesChildForm

from app.video_analyzer import VideoAnalyzer
from app.image_analyzer import ImageAnalyzer


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1900, 900)

        # Load background
        bg_image_path = "data/images/background.png"
        if os.path.exists(bg_image_path):
            pixmap = QPixmap(bg_image_path).scaled(1900, 900)
            palette = self.palette()
            palette.setBrush(QPalette.Background, QBrush(pixmap))
            self.setPalette(palette)

        self.setFixedSize(1900, 900)

        # === Buttons ===
        self.image_button = QPushButton('Анализ изображений', self)
        self.image_button.setGeometry(50, 9, 235, 70)
        self.image_button.clicked.connect(self.open_image_results_window)

        self.video_button = QPushButton('Видео анализ', self)
        self.video_button.setGeometry(300, 9, 200, 70)
        self.video_button.clicked.connect(self.open_video_results_window)

        self.db_button = QPushButton('База данных\nобнаружений', self)
        self.db_button.setGeometry(515, 9, 225, 70)
        self.db_button.clicked.connect(self.open_database_form)

        self.realtime_button = QPushButton('База данных\nреального времени', self)
        self.realtime_button.setGeometry(750, 9, 240, 70)
        self.realtime_button.clicked.connect(self.open_child_form)

        self.display_button = QPushButton('Проанализированные\nизображения', self)
        self.display_button.setGeometry(1000, 9, 380, 70)
        self.display_button.clicked.connect(self.open_image_display_form)

        self.setWindowTitle('Проект обнаружения дронов')
        self.show()

    # =====================
    #       Actions
    # =====================

    def open_image_results_window(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.jpg *.png)")
        files, _ = file_dialog.getOpenFileNames(self, "Выберите изображение", "")

        if files:
            analyzer = ImageAnalyzer(model_path="models/last.pt")
            analyzer.process_image(files[0])
            self.open_image_display_form()

    def open_video_results_window(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Videos (*.mp4 *.avi)")
        files, _ = file_dialog.getOpenFileNames(self, "Выберите видео", "")

        if files:
            video_analyzer = VideoAnalyzer(model_path="models/last.pt")
            video_analyzer.detect_and_save_objects(files[0])
            self.open_child_form()

    def open_child_form(self):
        self.child_form = ImagesChildForm()
        self.child_form.show()

    def open_image_display_form(self):
        self.image_display_form = ImageDisplayForm()
        self.image_display_form.show()

    def open_database_form(self):
        # No DB → We open the folder viewer
        self.image_display_form = ImageDisplayForm()
        self.image_display_form.show()
