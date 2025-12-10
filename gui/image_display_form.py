import os
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QGridLayout
from PyQt5.QtGui import QPixmap


class ImageDisplayForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("База данных проанализированных изображений")
        self.setGeometry(200, 200, 800, 600)

        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        grid = QGridLayout(scroll_widget)

        folder_path = "data/images"
        images = os.listdir(folder_path)

        row, col = 0, 0
        for name in images:
            img_path = os.path.join(folder_path, name)
            lbl = QLabel()
            px = QPixmap(img_path).scaled(300, 300)
            lbl.setPixmap(px)
            grid.addWidget(lbl, row, col)
            col += 1
            if col >= 3:
                col = 0
                row += 1

        self.setLayout(layout)
