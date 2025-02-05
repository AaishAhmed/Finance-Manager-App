import sys

from PyQt6.QtWidgets import QApplication, QMessageBox
from FinanceManager import FinanceManager
from data import init_db

def main():
    application = QApplication(sys.argv)

    if not init_db("expense.db"):
        QMessageBox.critical(None, "Error", "No database found. Terminating.")
        sys.exit(1)

    window = FinanceManager()
    window.show()

    sys.exit(application.exec())

if __name__ == "__main__":
    main()