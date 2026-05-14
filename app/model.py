import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt

class TableModel(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame()):
        super().__init__()
        self.df = df

    def rowCount(self, parent=None):
        return len(self.df)
    
    def columnCount(self, parent = None):
        return len(self.df.columns)
    
    # Affichage des données
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            val = self.df.iloc[index.row(), index.column()]
            if isinstance(val, float):
                return f"{val:.3f}"
            return str(val)
        return None
    
    # Affichage des en-têtes
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return str(self.df.columns[section])
        return str(section + 1)
    
    # Chargement d'un nouveau DataFrame
    def load(self, df):
        self.layoutAboutToBeChanged.emit()
        self.df = df
        self.layoutChanged.emit()