from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
sys.exit(app.exec())


# Your application won't reach here until you exit and the event
# loop has stopped.
