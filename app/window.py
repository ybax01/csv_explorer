from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Explorateur CSV")
        self.resize(1280, 720)

        centre = QWidget()
        self.setCentralWidget(centre)

        self.layout = QVBoxLayout(centre)