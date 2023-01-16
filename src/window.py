from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Neuron")
        self.setWindowIcon(QIcon("qt.png"))
    

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.show()
    sys.exit(app.exec())