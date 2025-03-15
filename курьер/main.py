import sys

from PyQt5.QtWidgets import QApplication
from database import db_session
from app.login.login_form import LoginForm


def main():
    db_session.global_init("database/database.db")
    app = QApplication(sys.argv)
    # screen = app.primaryScreen()
    ex = LoginForm()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()