import sys
from PyQt5.QtWidgets import QApplication, QWidget

from ui.admin_password import Ui_Form
from database import db_session
from models.admins import Admins
from app.admin.admin_form import AdminForm


class AdminPassword(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.check_admin)

    def check_admin(self):
        text = self.le_password.text()
        try:
            session = db_session.create_session()
            query = session.query(Admins).all()
            for i in query:
                if i.password == text:
                    self.a = AdminForm()
                    self.a.show()
                    self.close()

        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = AdminPassword()
    a.show()
    sys.exit(app.exec_())