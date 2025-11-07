"""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# REQUIREMENT - add import statements
from contact_list.contact_list import ContactList

# GIVEN:
from PySide6.QtWidgets import QApplication
import sys

# GIVEN:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactList()
    window.show()
    sys.exit(app.exec())