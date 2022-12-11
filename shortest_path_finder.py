from PyQt5 import QtCore, QtGui, QtWidgets
from grid_size import Ui_grid_size
from AstarSearch import find_shortest_path

class Ui_Form(object):
    def __init__(self, width, height):
        super(Ui_Form, self).__init__()
        self.WIDTH = width
        self.HEIGHT = height
        self.grid = [[1 for _ in range(self.HEIGHT)] for _ in range(self.WIDTH)]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 900)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(MainWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 613, 650))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1600, 850))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.pushButton = [[QtWidgets.QPushButton(self.gridLayoutWidget) 
                                            for _ in range(self.HEIGHT)]
                                            for _ in range(self.WIDTH)]
        for r in range(self.WIDTH):
            for c in range(self.HEIGHT):
                self.pushButton[r][c].setMinimumSize(QtCore.QSize(1, 1))
                self.pushButton[r][c].setStyleSheet("border: 2px solid grey;")
                self.pushButton[r][c].setStyleSheet("background-color: rgb(240, 240, 240);")
                self.pushButton[r][c].clicked.connect(lambda t, row=r, col=c : self.toggle_state(row,col))
                self.pushButton[r][c].setObjectName("pushButton{0}{1}".format(r,c))
                self.gridLayout.addWidget(self.pushButton[r][c], r, c, 1, 1)
        self.pushButton[0][0].setEnabled(False)
        self.pushButton[self.WIDTH-1][self.HEIGHT-1].setEnabled(False)
        self.pushButton[0][0].setStyleSheet("background-color: lightblue;")
        self.pushButton[self.WIDTH-1][self.HEIGHT-1].setStyleSheet("background-color: green;")

        
        self.verticalLayout.addLayout(self.gridLayout)
        self.button_container = QtWidgets.QFrame(self.frame)
        self.button_container.setMaximumHeight(90)
        self.button_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_container.setObjectName("button_container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_container)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.draw_btn = QtWidgets.QPushButton(self.button_container)
        self.draw_btn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.draw_btn.setFont(font)
        self.draw_btn.setObjectName("draw_btn")
        self.horizontalLayout.addWidget(self.draw_btn)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.button_container)
        self.horizontalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(MainWindow)
        self.draw_btn.clicked.connect(self.draw_path)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def toggle_state(self, x,y):
        if self.grid[x][y]:
            self.grid[x][y] = 0
            self.pushButton[x][y].setStyleSheet("background-color: black;")
        else:
            self.grid[x][y] = 1
            self.pushButton[x][y].setStyleSheet("background-color: rgb(240, 240, 240);")
    

    def draw_path(self):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if self.grid[x][y]:
                    self.pushButton[x][y].setStyleSheet("background-color: rgb(240, 240, 240);")          
                else:
                    self.pushButton[x][y].setStyleSheet("background-color: black;")
        path = find_shortest_path(self.grid, (0,0), (self.WIDTH-1, self.HEIGHT-1))
        for cell in path:
            self.pushButton[cell.x][cell.y].setStyleSheet("background-color: green;")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shortest Path Finder"))
        self.draw_btn.setText(_translate("MainWindow", "Draw path"))

class Linker():
    def __init__(self):
        self.w = 0
        self.h = 0
        dialog = QtWidgets.QDialog()
        self.ui = Ui_grid_size()
        self.ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()
        self.w = self.ui.width_value.value()
        self.h = self.ui.height_value.value()
        

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    linker = Linker()
    x = Linker.get_width(linker)
    y = Linker.get_height(linker)

    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form(x,y)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
