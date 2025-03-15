from PyQt5.QtWidgets import QMainWindow
from ui.login import Ui_MainWindow
from app.user.user_form import UserForm
from app.admin.admin_log_password import AdminPassword
from app.kurer.kurer_form import KurerForm


class LoginForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_user.clicked.connect(self.open_user_window)
        self.btn_admin.clicked.connect(self.open_admin_window)
        self.btn_kurer.clicked.connect(self.open_kurer_window)

    def open_user_window(self):
        self.a = UserForm()
        self.a.show()

    def open_admin_window(self):
        self.b = AdminPassword()
        self.b.show()

    def open_kurer_window(self):
        self.s = KurerForm()
        self.s.show()

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     lf = LoginForm()
#     lf.show()
#     sys.exit(app.exec_())