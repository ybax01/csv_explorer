from PyQt5.QtWidgets import (
    QComboBox, QHeaderView, QMainWindow, QTableView, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout , QLabel, QSplitter,
    QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt

from app.model import TableModel

import pandas as pd

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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

        self.btn_open.clicked.connect(self.open_file)


    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier CSV", "", "Fichiers CSV (*.csv)")
        if not path:
            return
        try:
            self.df = pd.read_csv(path)
            self.model.load(self.df)
            self.label_info.setText(f"{len(self.df)} rows, {len(self.df.columns)} columns")
            cols = list(self.df.columns)
            self.combo_x.clear()
            self.combo_x.addItems(cols)
            self.combo_y.clear()
            self.combo_y.addItems(cols)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Fichier non lu:\n{e}")
