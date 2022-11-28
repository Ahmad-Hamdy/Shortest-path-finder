from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_grid_size(QtCore.QObject):
    width = QtCore.pyqtSignal(int)
    height = QtCore.pyqtSignal(int)

    def setupUi(self, grid_size):
        grid_size.setObjectName("grid_size")
        grid_size.resize(400, 300)
        grid_size.setMinimumSize(QtCore.QSize(400, 300))
        grid_size.setMaximumSize(QtCore.QSize(400, 300))
        self.buttonBox = QtWidgets.QDialogButtonBox(grid_size)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.title = QtWidgets.QLabel(grid_size)
        self.title.setGeometry(QtCore.QRect(67, 10, 265, 49))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.width_x_height = QtWidgets.QLabel(grid_size)
        self.width_x_height.setGeometry(QtCore.QRect(100, 70, 200, 36))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.width_x_height.setFont(font)
        self.width_x_height.setObjectName("width_x_height")
        self.width_value = QtWidgets.QSpinBox(grid_size)
        self.width_value.setGeometry(QtCore.QRect(115, 140, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.width_value.setFont(font)
        self.width_value.setMaximum(80)
        self.width_value.setObjectName("width_value")
        self.height_value = QtWidgets.QSpinBox(grid_size)
        self.height_value.setGeometry(QtCore.QRect(225, 140, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.height_value.setFont(font)
        self.height_value.setMaximum(80)
        self.height_value.setObjectName("height_value")
        self.X_label = QtWidgets.QLabel(grid_size)
        self.X_label.setGeometry(QtCore.QRect(190, 140, 16, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.X_label.setFont(font)
        self.X_label.setObjectName("X_label")

        self.retranslateUi(grid_size)
        self.buttonBox.accepted.connect(grid_size.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(grid_size)

    def retranslateUi(self, grid_size):
        _translate = QtCore.QCoreApplication.translate
        grid_size.setWindowTitle(_translate("grid_size", "Grid Size"))
        self.title.setText(_translate("grid_size", "set the grid size"))
        self.width_x_height.setText(_translate("grid_size", "Width X Height"))
        self.X_label.setText(_translate("grid_size", "X"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    grid_size = QtWidgets.QDialog()
    ui = Ui_grid_size()
    ui.setupUi(grid_size)
    grid_size.show()
    sys.exit(app.exec_())
