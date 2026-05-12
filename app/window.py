from PyQt5.QtWidgets import (
    QHeaderView, QMainWindow, QTableView, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout , QLabel, QSplitter
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Explorateur CSV")
        self.resize(1280, 720)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        
        # Haute partie
        top_bar = QHBoxLayout()
        self.btn_open = QPushButton("Ouvrir CSV")
        self.label_info = QLabel("Aucun fichier ouvert")
        top_bar.addWidget(self.btn_open)
        top_bar.addWidget(self.label_info)
        top_bar.addStretch()  # Ajoute un espace flexible pour pousser les éléments vers la gauche
        layout.addLayout(top_bar)

        # Séparateur
        splitter = QSplitter(Qt.Vertical)

        self.table = QTableView()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        splitter.addWidget(self.table)


        
        layout.addWidget(splitter)
