import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Explorateur CSV")
window.resize(1280, 720)
window.show()

sys.exit(app.exec_())