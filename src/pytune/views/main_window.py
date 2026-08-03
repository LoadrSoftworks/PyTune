from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, Signal

class MainWindow(QMainWindow):
    # Custom signal emitted when a file is dropped
    file_dropped = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyTune - Package Inspector")
        self.resize(600, 400)
        self.setAcceptDrops(True)  # Enable drag and drop on the window

        # UI Setup
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Drag & Drop an .exe or .msi file here")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

    # Qt Drag & Drop Event Overrides
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.file_dropped.emit(file_path)  # Emit path to controller

    def update_result_text(self, text: str):
        self.label.setText(text)