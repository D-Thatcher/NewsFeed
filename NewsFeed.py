# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DanLa\PycharmProjects\NewsFeed\NewsFeed9.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1668, 867)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: white ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 1601, 741))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1599, 739))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 1601, 741))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 760, 1511, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.searchBar = QtWidgets.QLineEdit(self.frame)
        self.searchBar.setGeometry(QtCore.QRect(10, 10, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.searchBar.setFont(font)
        self.searchBar.setText("")
        self.searchBar.setObjectName("searchBar")
        self.highlightBar = QtWidgets.QLineEdit(self.frame)
        self.highlightBar.setGeometry(QtCore.QRect(440, 10, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.highlightBar.setFont(font)
        self.highlightBar.setText("")
        self.highlightBar.setObjectName("highlightBar")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(910, 0, 327, 70))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.presetHighlightBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.presetHighlightBox.setFont(font)
        self.presetHighlightBox.setObjectName("presetHighlightBox")
        self.gridLayout.addWidget(self.presetHighlightBox, 1, 1, 1, 1)
        self.liveUpdateBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.liveUpdateBox.setFont(font)
        self.liveUpdateBox.setObjectName("liveUpdateBox")
        self.gridLayout.addWidget(self.liveUpdateBox, 1, 0, 1, 1)
        self.twitterBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.twitterBox.setObjectName("twitterBox")
        self.gridLayout.addWidget(self.twitterBox, 2, 0, 1, 1)
        self.redditBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.redditBox.setObjectName("redditBox")
        self.gridLayout.addWidget(self.redditBox, 2, 1, 1, 1)
        self.updateButton = QtWidgets.QPushButton(self.frame)
        self.updateButton.setGeometry(QtCore.QRect(1300, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.frameButton = QtWidgets.QFrame(self.centralwidget)
        self.frameButton.setGeometry(QtCore.QRect(1550, 760, 51, 80))
        self.frameButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButton.setObjectName("frameButton")
        self.layoutWidget1 = QtWidgets.QWidget(self.frameButton)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 0, 31, 75))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hideButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hideButton.setFont(font)
        self.hideButton.setObjectName("hideButton")
        self.verticalLayout.addWidget(self.hideButton)
        self.showButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showButton.setFont(font)
        self.showButton.setObjectName("showButton")
        self.verticalLayout.addWidget(self.showButton)
        self.showButton.raise_()
        self.hideButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "News"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.highlightBar.setPlaceholderText(_translate("MainWindow", "Highlight..."))
        self.presetHighlightBox.setText(_translate("MainWindow", "Include Preset Highlight"))
        self.liveUpdateBox.setText(_translate("MainWindow", "Update On-The-Fly"))
        self.twitterBox.setText(_translate("MainWindow", "Twitter"))
        self.redditBox.setText(_translate("MainWindow", "Reddit"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.hideButton.setText(_translate("MainWindow", "<"))
        self.showButton.setText(_translate("MainWindow", ">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

