import os
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QGridLayout
from PyQt5.QtGui import QPixmap


class ImagesChildForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('База данных реального времени')
        self.setGeometry(200, 200, 800, 600)

        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        grid = QGridLayout(scroll_widget)

        folder_path = "data/Our_DataBase"
        images = os.listdir(folder_path)

        for index, name in enumerate(images):
            img_path = os.path.join(folder_path, name)
            lbl = QLabel()
            px = QPixmap(img_path).scaled(300, 300)
            lbl.setPixmap(px)

            row = index // 3
            col = index % 3
            grid.addWidget(lbl, row, col)

        self.setLayout(layout)
