from PyQt5.QtWidgets import QWidget
from ui.kurer_window import Ui_Form
import datetime

from database import db_session

from models.orders import Orders
from models.kurers import Kurers
from models.users import Users


class KurerForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rb = ''

        self.rb_1.clicked.connect(self.set_history_orders)
        self.rb_2.clicked.connect(self.set_history_orders)
        self.rb_3.clicked.connect(self.set_history_orders)

        self.btn_get_order.clicked.connect(self.get_order)

    def set_history_orders(self):
        self.rb = self.sender().text()
        self.te_new_orders.clear()
        self.lbl_time.clear()

        try:
            session = db_session.create_session()
            kurer = session.query(Kurers).filter(Kurers.kurer_name == self.rb).first()

            order_cur = session.query(Orders).filter(Orders.kurer == kurer.id, Orders.status == 2).first()

            if order_cur:
                user = session.query(Users).filter(Users.id == order_cur.user).first()
                address, phone, order_text = order_cur.text_order.split(' | ')
                self.te_new_orders.setText(f'Клиент: {user.user_name}\n\nАдрес: {address}\n\nНомер телефона: '
                                           f'{phone}\n\nЗаказ: {order_text}')
                self.te_new_orders.adjustSize()

                cur_time = datetime.datetime.now()
                end_time = datetime.datetime.strptime(order_cur.date_end, "%Y-%m-%d %H:%M")
                total_seconds = int((end_time - cur_time).total_seconds())
                minutes = (total_seconds % 3600) // 60
                self.lbl_time.setText(f'Осталось {minutes}\nминут')

            text = ''
            orders = session.query(Orders).filter(Orders.kurer == kurer.id, Orders.status == 1).all()
            for order in orders:
                if int(order.kurer) == int(kurer.id):
                    user_finish = session.query(Users).filter(Users.id == order.user).first()
                    text += f'{user_finish.user_name} | {order.text_order}\n\n'

            self.te_ended_orders.setText(text)

        except Exception as ex:
            print(ex)

    def get_order(self):
        self.te_new_orders.clear()
        try:
            session = db_session.create_session()
            kurer = session.query(Kurers).filter(Kurers.kurer_name == self.rb).first()
            order = session.query(Orders).filter(Orders.kurer == kurer.id, Orders.status == 2).first()

            time = int(self.lbl_time.text().split()[1])
            if time != 0:
                order.status = 1
                kurer.free = 1
                session.commit()
            else:
                self.lbl_time.setText('Вы не успели\nпринять заказ')
                self.te_new_orders.clear()
                order.status = 3
                kurer.free = 1
                session.commit()

        except Exception as ex:
            print(ex)

