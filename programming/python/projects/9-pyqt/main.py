from PyQt6.QtWidgets import *

app = QApplication([])
button = QPushButton('Click Me')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Ben is a noob!!!')
    alert.exec()

button.clicked.connect(on_button_clicked)
button.show()
app.exec()
