from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1180, 500)
                
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 841, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_comp = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_comp.setContentsMargins(0, 0, 0, 0)
        self.grid_comp.setObjectName("grid_comp")
        
        
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName("label_name")
        self.grid_comp.addWidget(self.label_name, 0, 0) 
        
        self.label_pb_convert = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pb_convert.setObjectName("label_pb_convert")
        self.grid_comp.addWidget(self.label_pb_convert, 0, 1)

        self.label_MW = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_MW.setObjectName("label_MW")
        self.grid_comp.addWidget(self.label_MW, 0, 2)
        
        self.label_C = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_C.setObjectName("label_C")
        self.grid_comp.addWidget(self.label_C, 0, 3)
        
        self.label_C_unit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_C_unit.setObjectName("label_C_unit")
        self.grid_comp.addWidget(self.label_C_unit, 0, 4)
        
        self.label_V = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_V.setObjectName("label_V")
        self.grid_comp.addWidget(self.label_V, 0, 5)
        
        self.label_V_unit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_V_unit.setObjectName("label_V_unit")
        self.grid_comp.addWidget(self.label_V_unit, 0, 6)
        
        self.label_pb_calc = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pb_calc.setObjectName("label_pb_calc")
        self.grid_comp.addWidget(self.label_pb_calc, 0, 7)
        
        self.label_mass = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_mass.setObjectName("label_mass")
        self.grid_comp.addWidget(self.label_mass, 0, 8)
        
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(False)
        
        
        
        self.vert_layout = QtWidgets.QVBoxLayout()

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
        
        
        self.vert_layout.addLayout(self.ToolLayout)
        self.vert_layout.addWidget(self.scrollArea)
        Form.setLayout(self.vert_layout)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Find Weight"))
        self.label_name.setText(_translate("Form", "|Component Name|"))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.adjustSize()
        self.label_pb_convert.setText(_translate("Form", "|Convert to MW|"))
        self.label_pb_convert.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pb_convert.adjustSize()
        self.label_MW.setText(_translate("Form", "|MW g/mol|"))
        self.label_MW.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MW.adjustSize()
        self.label_C.setText(_translate("Form", "|Concentration|"))
        self.label_C.setAlignment(QtCore.Qt.AlignCenter)
        self.label_C.adjustSize()
        self.label_C_unit.setText(_translate("Form", "|Concentration unit|"))
        self.label_C_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_C_unit.adjustSize()        
        self.label_V.setText(_translate("Form", "|Final Volume|"))
        self.label_V.setAlignment(QtCore.Qt.AlignCenter)
        self.label_V.adjustSize()
        self.label_V_unit.setText(_translate("Form", "|Volume unit|"))
        self.label_V_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_V_unit.adjustSize()
        self.label_pb_calc.setText(_translate("Form", "|Calculate|"))
        self.label_pb_calc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pb_calc.adjustSize()
        self.label_mass.setText(_translate("Form", "|Mass|"))
        self.label_mass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mass.adjustSize()
        self.gridLayoutWidget.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())