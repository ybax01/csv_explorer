from PyQt5.QtWidgets import (
    QComboBox, QHeaderView, QMainWindow, QTableView, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout , QLabel, QSplitter
)
from PyQt5.QtCore import Qt

from app.model import TableModel



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

        self.model = TableModel()
        self.table.setModel(self.model)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        splitter.addWidget(self.table)

        # Bas
        bottom = QWidget()
        bottom_layout = QVBoxLayout(bottom)

        controls = QHBoxLayout()
        controls.addWidget(QLabel("Type:"))
        self.combo_type = QComboBox()
        self.combo_type.addItems(["Histogramme", "Bar Chart", "Line Chart", "Scatter Plot"])
        controls.addWidget(self.combo_type)
        controls.addWidget(QLabel("X:"))
        self.combo_x = QComboBox()
        controls.addWidget(self.combo_x)
        controls.addWidget(QLabel("Y:"))
        self.combo_y = QComboBox()
        controls.addWidget(self.combo_y)
        self.btn_plot = QPushButton("Plot")
        controls.addWidget(self.btn_plot)
        controls.addStretch()
        bottom_layout.addLayout(controls)


        #chart
        self.chart_area = QLabel("Aperçu du graphique")
        self.chart_area.setAlignment(Qt.AlignCenter)

        bottom_layout.addWidget(self.chart_area)

        splitter.addWidget(bottom)

        splitter.setSizes([400, 400])

        layout.addWidget(splitter)
