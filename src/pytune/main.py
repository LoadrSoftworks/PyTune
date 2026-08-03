# PyTune 
# Author: LoadrSoftworks
# Description: PyTune main.py runtime script 

import sys
from PySide6.QtWidgets import QApplication
from pytune.views.main_window import MainWindow
from pytune.utils.getwinpack import inspect_package

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Slot function handling the dropped file path
    def handle_dropped_file(file_path: str):
        result = inspect_package(file_path)
        window.update_result_text(f"File: {file_path}\nType: {result}")

    # Connect view signal to handler
    window.file_dropped.connect(handle_dropped_file)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
