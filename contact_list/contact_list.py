"""The module defines the ContactList class.

This window allows users to add (and later remove) contacts using a simple table.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import (
    QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel,
    QVBoxLayout, QWidget, QTableWidgetItem
)
from PySide6.QtCore import Slot


class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""
        super().__init__()
        self.__initialize_widgets()

        # STEP 1: connect Add button (signal) to our private slot (event handler).
        self.add_button.clicked.connect(self.__on_add_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.

        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)

        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # -------------------- Step 1: Add Contact --------------------

    @Slot()
    def __on_add_contact(self):
        """
        Adds a contact to the table if both inputs contain text.
        Otherwise, displays a guidance message.

        Behavior:
            - If both non-empty:
                * Insert row at bottom of contact_table.
                * Column 0: Name, Column 1: Phone.
                * Status: "Added contact: {name}".
            - Else:
                * Status: "Please enter a contact name and phone number."
        """
        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and phone:
            row_position = self.contact_table.rowCount()
            self.contact_table.insertRow(row_position)
            self.contact_table.setItem(row_position, 0, QTableWidgetItem(name))
            self.contact_table.setItem(row_position, 1, QTableWidgetItem(phone))
            self.status_label.setText(f"Added contact: {name}")
        else:
            self.status_label.setText("Please enter a contact name and phone number.")
