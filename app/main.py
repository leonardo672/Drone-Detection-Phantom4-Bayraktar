import sys
from PyQt5.QtWidgets import QApplication
from windows.login_window import LoginWindow
from windows.main_window import MyWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    if login_window.exec_() == login_window.Accepted:
        main_window = MyWindow()
        main_window.show()
        sys.exit(app.exec_())
