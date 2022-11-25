from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 500)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1600, 850))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.pushButton = [
                        [QtWidgets.QPushButton(self.gridLayoutWidget) for _ in range(10)]
                                                                     for _ in range(10)]
        for r in range(10):
            for c in range(10):
                self.pushButton[r][c].setMinimumSize(QtCore.QSize(100, 100))
                self.pushButton[r][c].clicked.connect(lambda t, row=r, col=c : self.paint_black(row,col))
                self.pushButton[r][c].setObjectName("pushButton{0}{1}".format(r,c))
                self.gridLayout.addWidget(self.pushButton[r][c], r, c, 1, 1)
        self.pushButton[0][0].setEnabled(False)
        self.pushButton[9][9].setEnabled(False)
        self.pushButton[0][0].setStyleSheet("background-color: lightblue;")
        self.pushButton[9][9].setStyleSheet("background-color: green;")


        self.horizontalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def paint_black(self, x,y):
        self.pushButton[x][y].setStyleSheet("background-color: black;")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
