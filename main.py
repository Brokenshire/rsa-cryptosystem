# Copyright 2020 Jack Brokenshire

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Local imports
import sys

# Third-party imports
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow, QLabel, QPushButton, QLineEdit


class RSA(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(RSA, self).__init__(*args, **kwargs)
        self.build_interface()
    
    
    def build_interface(self):
        self.entry_lineedit = QLineEdit(self)
        self.entry_lineedit.move(30, 150)
        self.entry_lineedit.resize(120, 30)


def main():
    app = QApplication(sys.argv)
    window = RSA()
    window.setWindowTitle("RSA Cryptosystem")
    window.setGeometry(300, 300, 350, 400)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()