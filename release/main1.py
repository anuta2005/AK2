import sys
import sqlite3
from UI import addEditCoffeeForm

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class MyWidget(QtWidgets.QMainWindow, addEditCoffeeForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("../data/coffee1.sqlite")
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM coffees""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run1)

    def run(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def run1(self):
        cur = self.con.cursor()
        self.con.commit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

