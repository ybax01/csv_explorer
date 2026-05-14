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
        """
        self.chart_area = QLabel("Aperçu du graphique")
        self.chart_area.setAlignment(Qt.AlignCenter)
        bottom_layout.addWidget(self.chart_area)
        """

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        bottom_layout.addWidget(self.canvas)


        splitter.addWidget(bottom)

        splitter.setSizes([400, 400])

        layout.addWidget(splitter)

        self.btn_open.clicked.connect(self.open_file)

        self.btn_plot.clicked.connect(self.plot)


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


    def plot(self):
        col_x = self.combo_x.currentText()
        col_y = self.combo_y.currentText()
        chart_type = self.combo_type.currentText()

        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)
        
        try:
            if chart_type == "Histogramme":
                self.df[col_x].dropna().astype(float).hist(ax=ax, bins=25)
                ax.set_title(f"Histogramme de {col_x}")

            elif chart_type == "Bar Chart":
                self.df[col_x].value_counts().head(15).plot(kind="bar", ax=ax)

                ax.set_title(f"Bar Chart de {col_x}")

            elif chart_type == "Scatter Plot":
                x = pd.to_numeric(self.df[col_x], errors="coerce")
                y = pd.to_numeric(self.df[col_y], errors="coerce")
                ax.scatter(x, y, alpha=0.4)
                ax.set_xlabel(col_x)
                ax.set_ylabel(col_y)
                ax.set_title(f"{col_x} vs {col_y}")

            elif chart_type == "Line Chart":
                self.df[col_x].dropna().astype(float).reset_index(drop=True).plot(ax=ax)
                ax.set_title(f"Line — {col_x}")
            
        except Exception as e:
            ax.text(0.5, 0.5, f"Erreur: {e}", transform=ax.transAxes, ha="center")

        self.figure.tight_layout()
        self.canvas.draw()
