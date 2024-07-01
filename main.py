from PySide6.QtWidgets import QApplication
import sys
from src.logica.inicioTempolarm import Mysidebar

app = QApplication(sys.argv)
window = Mysidebar()
window.show()
sys.exit(app.exec())
