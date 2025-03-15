from PyQt5.QtWidgets import QWidget
from sqlalchemy import insert
import datetime

from ui.user_window import Ui_Form

from database import db_session

from models.orders import Orders
from models.users import Users
from models.kurers import Kurers


class UserForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rb = ''

        self.rb_1.clicked.connect(self.set_history_orders)
        self.rb_2.clicked.connect(self.set_history_orders)
        self.rb_3.clicked.connect(self.set_history_orders)

        self.btn_create_order.clicked.connect(self.create_order)

    def set_history_orders(self):
        self.rb = self.sender().text()

        try:
            session = db_session.create_session()
            orders = session.query(Orders).all()
            user = session.query(Users).filter(Users.user_name == self.rb).first()

            text = ''
            for order in orders:
                if order.user == user.id:
                    text += f'{order.text_order}\n\n'

            self.te_history_orders.setText(text)

        except Exception as ex:
            print(ex)

    def create_order(self):
        try:
            session = db_session.create_session()
            user = session.query(Users).filter(Users.user_name == self.rb).first()
            kurer = session.query(Kurers).filter(Kurers.free == 1).first()

            text_order = f'{self.le_address.text ()} | {self.le_phone.text ()} | {self.te_create_order.toPlainText ()}'

            if kurer:
                co = Orders(user=user.id, kurer=kurer.id,
                            date_start=f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
                            date_end=f'{(datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")}',
                            text_order=text_order, status=2)
                kurer_cur = session.query(Kurers).filter(Kurers.id == kurer.id).first()
                kurer_cur.free = 0
                self.te_create_order.clear()
                self.le_phone.clear()
                self.le_address.clear()

                session.add(co)
                session.commit()

            else:
                self.te_create_order.clear()
                self.te_create_order.setText('Извините, все курьеры заняты')
                self.le_phone.clear()
                self.le_address.clear()

        except Exception as ex:
            print(ex)