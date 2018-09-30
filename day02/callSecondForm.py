import sys
from PyQt5.QtWidgets import QApplication, QWidget
from secondForm import Ui_Form


class MyForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = MyForm()
    f.show()
    sys.exit(app.exec_())
