from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout , QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Explorateur CSV")
        self.resize(1280, 720)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        
        #Haute partie
        top_bar = QHBoxLayout()
        self.btn_open = QPushButton("Ouvrir CSV")
        self.label_info = QLabel("Aucun fichier ouvert")
        top_bar.addWidget(self.btn_open)
        top_bar.addWidget(self.label_info)
        layout.addLayout(top_bar)