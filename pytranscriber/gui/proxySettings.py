'''
   (C) 2020 ChuanyiLi
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit

from pytranscriber.util.util import MyUtil


class ProxySettingsWindow(object):
    def setupUi(self, dialog):
        dialog.setObjectName("proxyDialog")
        dialog.resize(577, 169)
        self.centralDialog = QtWidgets.QWidget(dialog)
        self.centralDialog.setObjectName("centralDialog")
        self.httpProxyLabel = QtWidgets.QLabel(self.centralDialog)
        self.httpProxyLabel.setGeometry(QtCore.QRect(20, 10, 531, 16))
        self.httpProxyLabel.setText("")
        self.httpProxyLabel.setObjectName("httpProxyLabel")

        self.httpPrefixEditor = QLineEdit(self.centralDialog)
        self.httpPrefixEditor.setGeometry(QtCore.QRect(20, 30, 121, 21))
        self.httpPrefixEditor.setText("socks5://127.0.0.1:")
        self.httpPrefixEditor.setEnabled(False)
        httpConfig, httpsConfig = MyUtil.loadProxySettings()
        httpPort = "" if len(httpConfig) == 0 else httpConfig["port"]
        httpsPort = "" if len(httpsConfig) == 0 else httpsConfig["port"]
        intValidator = QIntValidator(1, 65535, dialog)
        self.httpPortEditor = QLineEdit(self.centralDialog)
        self.httpPortEditor.setValidator(intValidator)
        self.httpPortEditor.setGeometry(QtCore.QRect(150, 30, 71, 21))
        self.httpPortEditor.setText(httpPort)

        self.httpsProxyLabel = QtWidgets.QLabel(self.centralDialog)
        self.httpsProxyLabel.setGeometry(QtCore.QRect(20, 60, 531, 16))
        self.httpsProxyLabel.setText("")
        self.httpsProxyLabel.setObjectName("httpsProxyLabel")

        self.httpsPrefixEditor = QLineEdit(self.centralDialog)
        self.httpsPrefixEditor.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.httpsPrefixEditor.setText("socks5://127.0.0.1:")
        self.httpsPrefixEditor.setEnabled(False)

        self.httpsPortEditor = QLineEdit(self.centralDialog)
        self.httpsPortEditor.setValidator(intValidator)
        self.httpsPortEditor.setGeometry(QtCore.QRect(150, 80, 71, 21))
        self.httpsPortEditor.setText(httpsPort)

        self.saveButton = QtWidgets.QPushButton(self.centralDialog)
        self.saveButton.setEnabled(True)
        self.saveButton.setGeometry(QtCore.QRect(220, 120, 113, 32))

        self.resetButton = QtWidgets.QPushButton(self.centralDialog)
        if httpPort == "" and httpsPort == "":
            self.resetButton.setEnabled(False)
        else:
            self.resetButton.setEnabled(True)
        self.resetButton.setGeometry(QtCore.QRect(10, 120, 100, 32))

        self.saveButtonPrompt = QtWidgets.QLabel(self.centralDialog)
        self.saveButtonPrompt.setGeometry(QtCore.QRect(340, 130, 211, 16))
        self.saveButtonPrompt.setText("")
        self.saveButtonPrompt.setObjectName("saveButtonPrompt")

        

        self.retranslateUi(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("proxyDialog", "Proxy Settings"))
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        self.httpProxyLabel.setText(_translate("proxyDialog",
                                               "http proxy. current only supports local socks5 proxy, so just input the port(0~65535)"))
        self.httpsProxyLabel.setText(_translate("proxyDialog",
                                                "https proxy. current only supports local socks5 proxy, so just input the port(0~65535)"))
        self.saveButton.setText(_translate("proxyDialog", "Save"))
        self.resetButton.setText(_translate("proxyDialog", "Reset Proxy"))
