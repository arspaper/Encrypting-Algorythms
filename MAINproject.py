from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import random
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 30, 281, 231))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.textChanged.connect(self.on_plain_text_changed)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 290, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(
            QRegExpValidator(QRegExp("[A-Za-z0-9]+"), self.lineEdit))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 200, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 320, 71, 16))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 340, 281, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 150, 101, 131))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 290, 101, 131))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 430, 101, 141))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(310, 30, 200, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(310, 50, 200, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(310, 70, 200, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(310, 90, 200, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(310, 110, 200, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(310, 130, 200, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 200, 21))
        self.label_4.setObjectName("label_4")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(20, 580, 281, 20))
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setStyleSheet("color: red")
        self.errorLabel.setVisible(False)
        self.label_2_keys = QtWidgets.QLabel(self.centralwidget)
        self.label_2_keys.setGeometry(QtCore.QRect(20, 270, 141, 16))
        self.label_2_keys.setObjectName("label_2_keys")
        self.label_2_keys.setText("Input 2 keys/Pattern")
        self.label_2_keys.setVisible(False)
        self.lineEdit_2_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2_1.setGeometry(QtCore.QRect(20, 290, 131, 20))
        self.lineEdit_2_1.setObjectName("lineEdit_2_1")
        self.lineEdit_2_1.setVisible(False)
        self.lineEdit_2_1.setValidator(
            QRegExpValidator(QRegExp("[A-Za-z0-9]+"), self.lineEdit_2_1))
        self.lineEdit_2_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2_2.setGeometry(QtCore.QRect(160, 290, 131, 20))
        self.lineEdit_2_2.setObjectName("lineEdit_2_2")
        self.lineEdit_2_2.setVisible(False)
        self.lineEdit_2_2.setValidator(
            QRegExpValidator(QRegExp("[A-Za-z0-9]+"), self.lineEdit_2_2))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_encrypt_button_clicked)
        self.pushButton_2.clicked.connect(self.on_decrypt_button_clicked)
        self.pushButton_3.clicked.connect(self.on_clear_button_clicked)
        self.radioButton.clicked.connect(self.on_caesar_cipher_selected)
        self.radioButton_2.clicked.connect(self.on_polybius_square_selected)
        self.radioButton_3.clicked.connect(self.on_vigenere_cipher_selected)
        self.radioButton_6.clicked.connect(self.on_zaza_cipher_selected)
        self.radioButton_5.clicked.connect(self.on_ap_cipher_selected)
        self.radioButton_6.clicked.connect(self.on_dreferd_cipher_selected)


    def on_plain_text_changed(self):
        cursor = self.plainTextEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        plain_text = self.plainTextEdit.toPlainText()

        new_text = ''.join(
            char if (char.isalnum() or char == '-' or char == " ") and char.isascii() else '' for char in
            plain_text)
        if new_text != plain_text:
            cursor.movePosition(QtGui.QTextCursor.Start)
            cursor.movePosition(QtGui.QTextCursor.End,
                                QtGui.QTextCursor.KeepAnchor)
            cursor.removeSelectedText()
            cursor.insertText(new_text)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Input Text"))
        self.label_2.setText(_translate("MainWindow", "Input Key/Pattern"))
        self.label_3.setText(_translate("MainWindow", "Output Text"))
        self.pushButton.setText(_translate("MainWindow", "Encrypt"))
        self.pushButton_2.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.radioButton.setText(_translate("MainWindow", "Caesar Cipher"))
        self.radioButton_2.setText(_translate("MainWindow", "Polybius Square"))
        self.radioButton_3.setText(_translate("MainWindow", "Vigenere Cipher"))
        self.radioButton_4.setText(_translate("MainWindow", "“Zaza” Cipher"))
        self.radioButton_5.setText(_translate("MainWindow", "“ap” Cipher"))
        self.radioButton_6.setText(_translate("MainWindow", "“Dreferd” Cipher"))
        self.label_4.setText(_translate("MainWindow", "Choose Cipher"))

    def on_encrypt_button_clicked(self):
        input_text = self.plainTextEdit.toPlainText().upper()
        key = self.lineEdit.text()
        if not self.is_cipher_selected():
            self.show_error("Select cipher")
            return
        if self.radioButton.isChecked() and (not key.isdigit()):
            self.show_error(
                "Invalid key value. The key must consist of digits.")
            return
        if (self.radioButton.isChecked() or self.radioButton_3.isChecked() or self.radioButton_4.isChecked() or self.radioButton_5.isChecked()) and not key:
            self.show_error("Enter key")
            return
        if not input_text:
            self.show_error("Enter input text")
            return
        self.errorLabel.setVisible(False)
        if self.radioButton.isChecked():
            if input_text[0].isdigit():
                self.show_error(
                    "Unable to encrypt: Input text contains only digits with the first character being a digit.")
                return
            self.errorLabel.setVisible(False)
            encrypted_text = self.encrypt_caesar(input_text, int(key))
        elif self.radioButton_2.isChecked():
            if input_text[0].isdigit():
                self.show_error(
                    "Unable to encrypt: Input text contains only digits with the first character being a digit.")
                return
            self.errorLabel.setVisible(False)
            encrypted_text = self.polybius_cipher(input_text)
        elif self.radioButton_3.isChecked():
            if input_text[0].isdigit():
                self.show_error(
                    "Unable to encrypt: Input text contains only digits with the first character being a digit.")
                return
            self.errorLabel.setVisible(False)
            encrypted_text = self.encrypt_vigenere(input_text, key)
        elif self.radioButton_6.isChecked():
            self.errorLabel.setVisible(False)
            key = self.lineEdit_2_1.text()
            key1 = self.lineEdit_2_2.text()
            if (not key or not key1) or (not key and not key1):
                self.show_error("Enter key")
                return
            encrypted_text = self.dreferd_encrypt(input_text, int(key), int(key1))
            self.textBrowser.setPlainText(encrypted_text)
        elif self.radioButton_5.isChecked():
            key = self.lineEdit.text()
            encrypted_text = self.encryptAP(input_text, key)
            self.textBrowser.setPlainText(encrypted_text)
        elif self.radioButton_4.isChecked():
            self.errorLabel.setVisible(False)
            encrypted_text = self.encryptZA(input_text, int(key))

        self.textBrowser.setPlainText(encrypted_text)

    def on_decrypt_button_clicked(self):
        input_text = self.plainTextEdit.toPlainText().upper()
        key = self.lineEdit.text()
        if not self.is_cipher_selected():
            self.show_error("Select cipher")
            return
        if self.radioButton.isChecked() and (not key.isdigit()):
            self.show_error(
                "Invalid key value. The key must consist of digits.")
            return
        if (self.radioButton.isChecked()  or self.radioButton_3.isChecked() or self.radioButton_4.isChecked() or self.radioButton_5.isChecked()) and not key:
            self.show_error("Enter key")
            return
        if not input_text:
            self.show_error("Enter input text")
            return
        self.errorLabel.setVisible(False)
        if self.radioButton.isChecked():
            if input_text[0].isdigit():
                self.show_error(
                    "Unable to decrypt: Input text contains only digits with the first character being a digit.")
                return
            self.errorLabel.setVisible(False)
            decrypted_text = self.decrypt_caesar(input_text, int(key))
        elif self.radioButton_2.isChecked():
            self.errorLabel.setVisible(False)
            if input_text[0].isalpha():
                self.show_error(
                                "Unable to decrypt: Input text contains only letters with the first character being a letter")
                return
            decrypted_text = self.polybius_decipher(input_text)
        elif self.radioButton_3.isChecked():
            if input_text[0].isdigit():
                self.show_error(
                    "Unable to decrypt: Input text contains only digits with the first character being a digit.")
                return
            self.errorLabel.setVisible(False)
            decrypted_text = self.decrypt_vigenere(input_text, key)
        elif self.radioButton_6.isChecked():
            self.errorLabel.setVisible(False)
            key = self.lineEdit_2_1.text()
            key1 = self.lineEdit_2_2.text()
            if (not key or not key1) or (not key and not key1):
                self.show_error("Enter key")
                return
            if input_text[0].isdigit():
                self.show_error(
                    "Unable to decrypt: Input text contains only digits with the first character being a digit.")
                return
            decrypted_text = self.dreferd_decrypt(input_text, int(key), int(key1))
            self.textBrowser.setPlainText(decrypted_text)
        elif self.radioButton_5.isChecked():
            self.errorLabel.setVisible(False)
            key = self.lineEdit.text()
            decrypted_text = self.decryptAP(input_text, key)
            self.textBrowser.setPlainText(decrypted_text)
        elif self.radioButton_4.isChecked():
            self.errorLabel.setVisible(False)
            decrypted_text = self.decryptZA(input_text, int(key))

        self.textBrowser.setPlainText(decrypted_text)

    def is_cipher_selected(self):
        return any([
            self.radioButton.isChecked(),
            self.radioButton_2.isChecked(),
            self.radioButton_3.isChecked(),
            self.radioButton_6.isChecked(),
            self.radioButton_5.isChecked(),
            self.radioButton_4.isChecked()
        ])

    def show_error(self, message):
        self.errorLabel.setText(message)
        self.errorLabel.setVisible(True)

    def hide_error(self):
        self.errorLabel.clear()
        self.errorLabel.setVisible(False)

    def on_polybius_square_selected(self):
        self.lineEdit.setVisible(False)
        self.label_2.setVisible(False)

    def on_clear_button_clicked(self):
        self.plainTextEdit.clear()
        self.lineEdit.clear()
        self.textBrowser.clear()
        self.lineEdit_2_1.clear()
        self.lineEdit_2_2.clear()
        self.errorLabel.setVisible(False)

    def on_caesar_cipher_selected(self):
        self.lineEdit.setVisible(True)
        self.label_2.setVisible(True)
        self.label_2_keys.setVisible(False)
        self.lineEdit_2_1.setVisible(False)
        self.lineEdit_2_2.setVisible(False)
    def on_polybius_square_selected(self):
        self.lineEdit.setVisible(False)
        self.label_2.setVisible(False)
        self.label_2_keys.setVisible(False)
        self.lineEdit_2_1.setVisible(False)
        self.lineEdit_2_2.setVisible(False)
    def on_vigenere_cipher_selected(self):
        self.lineEdit.setVisible(True)
        self.label_2.setVisible(True)
        self.label_2_keys.setVisible(False)
        self.lineEdit_2_1.setVisible(False)
        self.lineEdit_2_2.setVisible(False)
    def on_dreferd_cipher_selected(self):
        self.label_3.setVisible(True)
        self.lineEdit.setVisible(False)
        self.label_2.setVisible(False)
        self.label_2_keys.setVisible(True)
        self.lineEdit_2_1.setVisible(True)
        self.lineEdit_2_2.setVisible(True)
    def on_ap_cipher_selected(self):
        self.lineEdit.setVisible(True)
        self.label_2.setVisible(True)
        self.label_2_keys.setVisible(False)
        self.lineEdit_2_1.setVisible(False)
        self.lineEdit_2_2.setVisible(False)
    def on_zaza_cipher_selected(self):
        self.lineEdit.setVisible(True)
        self.label_2.setVisible(True)
        self.label_2_keys.setVisible(False)
        self.lineEdit_2_1.setVisible(False)
        self.lineEdit_2_2.setVisible(False)

    def encrypt_caesar(self, text, key):
        result = ''
        for char in text:
            if char.isalpha():
                shift = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - shift + key) % 26 + shift)
            else:
                result += char
        return result

    def decrypt_caesar(self, text, key):
        return self.encrypt_caesar(text, -key)

    def encrypt_vigenere(self, text, key):
        result = ''
        key = key.lower()
        key_index = 0

        for char in text:
            if char.isalpha():
                shift = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - shift + ord(key[key_index]) - ord('a')) % 26 + shift)
                key_index = (key_index + 1) % len(key)
            else:
                result += char
        return result

    def decrypt_vigenere(self, text, key):
        result = ''
        key = key.lower()
        key_index = 0

        for char in text:
            if char.isalpha():
                shift = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - shift - (ord(key[key_index]) - ord('a'))) % 26 + shift)
                key_index = (key_index + 1) % len(key)
            else:
                result += char
        return result

    def polybius_cipher(self, text):
        polybius_square = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']
        ]

        result = ''
        for char in text:
            if char.isalpha() and char.isascii():
                if char == 'J':
                    char = 'I'
                for row in range(5):
                    for col in range(5):
                        if polybius_square[row][col] == char:
                            result += f'{row + 1}{col + 1} '
            else:
                result += char
        return result.rstrip()

    def polybius_decipher(self, text):
        polybius_square = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'K'],
            ['L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']
        ]

        result = ''
        pairs = text.split()
        for pair in pairs:
            row, col = int(pair[0]) - 1, int(pair[1]) - 1
            result += polybius_square[row][col]

        return result

    def dreferd_encrypt(self, text, key1, key2):
        encrypt_numbers = []
        for i, char in enumerate(text):
            ascii_code = ord(char)
            if i % 2 == 0:
                encrypted_code = ascii_code ^ key1
            else:
                encrypted_code = ascii_code ^ key2
            encrypt_numbers.append(str(encrypted_code))
        encrypt_numbers = '-'.join(encrypt_numbers)
        return encrypt_numbers

    def dreferd_decrypt(self, encrypt_numbers, key1, key2):
        encrypt_numbers = encrypt_numbers.split('-')

        decrypted_text = ""
        for i, encrypted_code in enumerate(encrypt_numbers):
            encrypted_code = int(encrypted_code)
            if i % 2 == 0:
                decrypted_code = encrypted_code ^ key1
            else:
                decrypted_code = encrypted_code ^ key2

            decrypted_text += chr(decrypted_code)
        return decrypted_text

    def encryptAP(self,text, key):
        if not key.isascii() or not text.isascii():
            return "NOT ASCII"

        text = text.upper()
        key = key.upper()
        out_line = ""
        key_length = len(key)
        shifts = [ord(chrc) % 26 for chrc in key]
        index = 0

        for chrc in text:
            shift = shifts[index]
            if chrc.isalpha():
                out_line += chr((ord(chrc) - 65 + shift) % 26 + 65)
            elif chrc.isdigit():
                out_line += chr((ord(chrc) - 48 + shift) % 10 + 48)
            else:
                out_line += chrc
            index = (index + 1) % key_length

        return out_line

    def decryptAP(self,text, key):
        if not key.isascii() or not text.isascii():
            return "NOT ASCII"

        text = text.upper()
        key = key.upper()
        out_line = ""
        key_length = len(key)
        shifts = [ord(chrc) % 26 for chrc in key]
        index = 0

        for chrc in text:
            shift = shifts[index]
            if chrc.isalpha():
                out_line += chr((ord(chrc) - 65 - shift + 26) % 26 + 65)
            elif chrc.isdigit():
                out_line += chr((ord(chrc) - 48 - shift + 10) % 10 + 48)
            else:
                out_line += chrc
            index = (index + 1) % key_length

        return out_line

    def encryptZA(self, txt, pattern):
        encryptionCharacters = r"#$%+()'*&,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_ `abcdefghijklmnopqrstuvwxyz{|}~"
        l = list(encryptionCharacters)
        random.shuffle(l)
        mydata = ''.join(l)
        letterlower = 'abcdefghijklmnopqrstuvwxyz'
        letterupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #pattern = pattern.split()
        out_txt = ""
        shift = 0
        for chrc in txt:
            if chrc in letterlower:
                chrc = chrc.upper()
            elif chrc in letterupper:
                chrc = chrc.lower()
            out_txt += self.encrypt_caesar(chrc, len(pattern[shift]), mydata)
            shift += 1
        return out_txt

    def decryptZA(self, txt, pattern):
        encryptionCharacters = r"#$%+()'*&,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_ `abcdefghijklmnopqrstuvwxyz{|}~"
        l = list(encryptionCharacters)
        random.shuffle(l)
        mydata = ''.join(l)
        letterlower = 'abcdefghijklmnopqrstuvwxyz'
        letterupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # pattern = pattern.split()
        out_txt = ""
        shift = 0
        for chrc in txt:
            if chrc in letterlower:
                chrc = chrc.upper()
            elif chrc in letterupper:
                chrc = chrc.lower()
            out_txt += self.decrypt_caesar(chrc, len(pattern[shift]), mydata)
            shift += 1
        return out_txt

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
