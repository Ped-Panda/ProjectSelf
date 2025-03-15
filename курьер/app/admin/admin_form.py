import sys
import xlsxwriter

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from ui.admin_window import Ui_Form

from database import db_session

from models.orders import Orders
from models.kurers import Kurers
from models.users import Users


class AdminForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.set_kurers()
        self.btn_report.clicked.connect(self.report)

    def set_kurers(self):
        session = db_session.create_session()
        kurers = session.query(Kurers).all()
        for kurer in kurers:
            self.check_kurer.addItem(kurer.kurer_name)

    def report(self):
        kurer_checked = self.check_kurer.currentText()

        try:
            session = db_session.create_session()
            kurer = session.query(Kurers).filter(Kurers.kurer_name == kurer_checked).first()

            orders_finish = []
            orders = session.query(Orders).filter(Orders.kurer == kurer.id, Orders.status == 1).all()
            for order in orders:
                if int(order.kurer) == int(kurer.id):
                    user_finish = session.query(Users).filter(Users.id == order.user).first()
                    orders_finish.append(f'{user_finish.user_name} | {order.text_order}\n\n')

            self.lbl_count_orders.setText(f'{len(orders_finish)}')

            # Создание отчёта в exel
            workbook = xlsxwriter.Workbook(f'app/reports/report_about_kurers_{kurer_checked}.xlsx')
            worksheet = workbook.add_worksheet()

            worksheet.set_column('A:A', 20)
            worksheet.set_column('B:B', 20)
            worksheet.set_column('C:C', 20)
            worksheet.set_column('D:D', 100)

            worksheet.write('A1', 'ФИО')
            worksheet.write('B1', 'Адрес')
            worksheet.write('C1', 'Номер телефона')
            worksheet.write('D1', 'Заказ')

            row = 1
            for order_finish in orders_finish:
                fio, address, phone, cur_order = order_finish.strip().split(' | ')
                worksheet.write(row, 0, fio)
                worksheet.write(row, 1, address)
                worksheet.write(row, 2, phone)
                worksheet.write(row, 3, cur_order)
                row += 1

            workbook.close()

            # Заполнение TableWidget
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setRowCount(len(orders_finish))

            self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Адрес", "Номер телефона", "Заказ"])

            for i, order_finish in enumerate(orders_finish):
                fio, address, phone, cur_order = order_finish.strip().split(' | ')

                self.tableWidget.setItem(i, 0, QTableWidgetItem(fio))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(address))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(phone))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(cur_order))

            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.resizeColumnsToContents()

        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = AdminForm()
    a.show()
    sys.exit(app.exec_())