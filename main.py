import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQT5 GUI Test")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a QLabel
        label = QLabel("Hi, my name is Ash!", self)
        # Center-align text both horizontally and vertically
        label.setAlignment(Qt.AlignCenter)

        # Use a QVBoxLayout to center the QLabel in the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        central_widget.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
