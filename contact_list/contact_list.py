"""The module defines the ContactList class.

This window allows users to add contacts using a simple table.

Step 1: UI scaffold is provided in __initialize_widgets() (DO NOT EDIT).
Step 2: Add Contact event handling (signal/slot) is implemented.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import (
    QMainWindow,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QLabel,
    QVBoxLayout,
    QWidget,
    QTableWidgetItem,
)
from PySide6.QtCore import Slot


class ContactList(QMainWindow):
    """
    Provides a UI to manage contacts.

      - Step 1: The given UI is created in __initialize_widgets() (DO NOT EDIT).
      - Step 2: The Add Contact Slot is implemented and wired to the Add button.
    """

    def __init__(self):
        """Initializes a new instance of the ContactList class."""
        super().__init__()
        self.__initialize_widgets()

        # Step 2: Connect the Add button's clicked signal to the private Slot.
        self.add_button.clicked.connect(self.__on_add_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.

        Step 1: This method is provided by the activity as the starting UI layout.
                 It should not be modified.
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

    # -----------------------------
    # Step 2: Add Contact (private Slot)
    # -----------------------------
    @Slot()
    def __on_add_contact(self):
        """
        Adds a contact to the table if both inputs contain text.
        Otherwise, displays the required message in the status label.

        Messages:
            - Success: "Added contact: {name}"
            - Missing input: "Please enter a contact name and phone number."
        """
        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if len(name) > 0 and len(phone) > 0:
            row_position = self.contact_table.rowCount()
            self.contact_table.insertRow(row_position)

            # Create and assign table items (Name, Phone).
            self.contact_table.setItem(row_position, 0, QTableWidgetItem(name))
            self.contact_table.setItem(row_position, 1, QTableWidgetItem(phone))

            # Update the status label (exact wording per Activity).
            self.status_label.setText(f"Added contact: {name}")
        else:
            self.status_label.setText("Please enter a contact name and phone number.")
