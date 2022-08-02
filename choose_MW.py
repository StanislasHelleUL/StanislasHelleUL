# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\choose_MW.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MW_list_Form(object):
    def setupUi(self, MW_list_Form):
        MW_list_Form.setObjectName("MW_list_Form")
        MW_list_Form.resize(458, 300)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        MW_list_Form.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(MW_list_Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 443, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.chooseMW_vLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.chooseMW_vLayout.setContentsMargins(0, 0, 0, 0)
        self.chooseMW_vLayout.setObjectName("chooseMW_vLayout")
        self.MW_list_lb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.MW_list_lb.setObjectName("MW_list_lb")
        self.chooseMW_vLayout.addWidget(self.MW_list_lb)
        self.label_choose = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_choose.setAlignment(QtCore.Qt.AlignCenter)
        self.label_choose.setObjectName("label_choose")
        self.chooseMW_vLayout.addWidget(self.label_choose)
        self.spinBox_indexes = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_indexes.setMinimum(0)
        self.spinBox_indexes.setObjectName("spinBox_indexes")
        self.chooseMW_vLayout.addWidget(self.spinBox_indexes)
        self.OK_pb = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OK_pb.setObjectName("OK_pb")
        self.chooseMW_vLayout.addWidget(self.OK_pb)

        self.retranslateUi(MW_list_Form)
        QtCore.QMetaObject.connectSlotsByName(MW_list_Form)

    def retranslateUi(self, MW_list_Form):
        _translate = QtCore.QCoreApplication.translate
        MW_list_Form.setWindowTitle(_translate("MW_list_Form", "Choose one molecular weight"))
        self.MW_list_lb.setText(_translate("MW_list_Form", ""))
        self.label_choose.setText(_translate("MW_list_Form", "Please choose the MW value index\n"
"which seems correct to you:"))
        self.OK_pb.setText(_translate("MW_list_Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MW_list_Form = QtWidgets.QWidget()
    ui = Ui_MW_list_Form()
    ui.setupUi(MW_list_Form)
    MW_list_Form.show()
    sys.exit(app.exec_())

