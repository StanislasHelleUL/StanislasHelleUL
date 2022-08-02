from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UniProtForm(object):
    def setupUi(self, UniProtForm):
        UniProtForm.setObjectName("UniProtForm")
        UniProtForm.resize(710, 900)
        self.VBoxLayout = QtWidgets.QVBoxLayout(UniProtForm)
        
        self.ToolLayout = QtWidgets.QHBoxLayout()
        self.ToolLayout.setAlignment(QtCore.Qt.AlignLeft)
        
        
        self.OpenBtn = QtWidgets.QToolButton()
        self.OpenIcon = QtGui.QIcon()
        self.OpenIcon.addPixmap(QtGui.QPixmap("data/Open_symbol.png"))
        self.OpenBtn.setIcon(self.OpenIcon)
        self.OpenBtn.setFixedSize(30, 30)
        self.OpenBtn.setIconSize(self.OpenBtn.size())
        self.OpenBtn.setShortcut('Ctrl+O')
        self.OpenBtn.setToolTip('Open\tCtrl+O')
        self.ToolLayout.addWidget(self.OpenBtn)
        
        self.saveBtn = QtWidgets.QToolButton()
        self.saveIcon = QtGui.QIcon()
        self.saveIcon.addPixmap(QtGui.QPixmap("data/Save_symbol.png"))
        self.saveBtn.setIcon(self.saveIcon)
        self.saveBtn.setFixedSize(30, 30)
        self.saveBtn.setIconSize(self.saveBtn.size())
        self.saveBtn.setShortcut('Ctrl+S')
        self.saveBtn.setToolTip('Save\tCtrl+S')
        self.ToolLayout.addWidget(self.saveBtn)
        
        self.saveAsBtn = QtWidgets.QToolButton()
        self.saveAsIcon = QtGui.QIcon()
        self.saveAsIcon.addPixmap(QtGui.QPixmap("data/SaveAs_symbol.png"))
        self.saveAsBtn.setIcon(self.saveAsIcon)
        self.saveAsBtn.setFixedSize(30, 30)
        self.saveAsBtn.setIconSize(self.saveBtn.size())
        self.saveAsBtn.setShortcut('Ctrl+Shift+S')
        self.saveAsBtn.setToolTip('Save as\tCtrl+Shift+S')
        self.ToolLayout.addWidget(self.saveAsBtn)
        
        self.LightBtn = QtWidgets.QToolButton()
        self.LightIcon = QtGui.QIcon()
        self.LightIcon.addPixmap(QtGui.QPixmap("data/Light_symbol.png"))
        self.LightBtn.setIcon(self.LightIcon)
        self.LightBtn.setFixedSize(30, 30)
        self.LightBtn.setIconSize(self.LightBtn.size())
        self.LightBtn.setShortcut('Ctrl+Shift+L')
        self.LightBtn.setToolTip('Light mode\tCtrl+Shift+L')
        self.ToolLayout.addWidget(self.LightBtn)
        
        self.DarkBtn = QtWidgets.QToolButton()
        self.DarkIcon = QtGui.QIcon()
        self.DarkIcon.addPixmap(QtGui.QPixmap("data/Dark_symbol.png"))
        self.DarkBtn.setIcon(self.DarkIcon)
        self.DarkBtn.setFixedSize(30, 30)
        self.DarkBtn.setIconSize(self.DarkBtn.size())
        self.DarkBtn.setShortcut('Ctrl+Shift+D')
        self.DarkBtn.setToolTip('Dark mode\tCtrl+Shift+D')
        self.ToolLayout.addWidget(self.DarkBtn)
        
        self.HelpBtn = QtWidgets.QToolButton()
        self.HelpIcon = QtGui.QIcon()
        self.HelpIcon.addPixmap(QtGui.QPixmap("data/Help_symbol.png"))
        self.HelpBtn.setIcon(self.HelpIcon)
        self.HelpBtn.setFixedSize(30, 30)
        self.HelpBtn.setIconSize(self.HelpBtn.size())
        self.HelpBtn.setShortcut('Ctrl+H')
        self.HelpBtn.setToolTip('Help\tCtrl+H')
        self.ToolLayout.addWidget(self.HelpBtn)
        
        
        
        self.VBoxLayout.addLayout(self.ToolLayout)
        
        self.UniProtScrollArea = QtWidgets.QScrollArea()
        self.UniProtScrollArea.setGeometry(QtCore.QRect(10, 10, 690, 880))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.UniProtScrollArea.setFont(font)
        self.UniProtScrollArea.setWidgetResizable(False)
        self.UniProtScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.UniProtScrollArea.setObjectName("UniProtScrollArea")
        self.UniProtScrollAreaWidget = QtWidgets.QWidget()
        self.UniProtScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 688, 878))
        self.UniProtScrollAreaWidget.setObjectName("UniProtScrollAreaWidget")
        self.UniProtTextLabel = QtWidgets.QLabel(self.UniProtScrollAreaWidget)
        self.UniProtTextLabel.setGeometry(QtCore.QRect(6, 12, 685, 875))
        self.UniProtTextLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.UniProtTextLabel.setObjectName("UniProtTextLabel")
        self.UniProtScrollArea.setWidget(self.UniProtScrollAreaWidget)
        self.VBoxLayout.addWidget(self.UniProtScrollArea)
        

        self.retranslateUi(UniProtForm)
        QtCore.QMetaObject.connectSlotsByName(UniProtForm)

    def retranslateUi(self, UniProtForm):
        _translate = QtCore.QCoreApplication.translate
        UniProtForm.setWindowTitle(_translate("UniProtForm", "Protein information"))
        self.UniProtTextLabel.setText(_translate("UniProtForm", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UniProtForm = QtWidgets.QWidget()
    ui = Ui_UniProtForm()
    ui.setupUi(UniProtForm)
    UniProtForm.show()
    sys.exit(app.exec_())