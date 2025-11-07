"""The module defines the ContactList class.

This window allows users to add and remove contacts using a simple table.

Step 1: UI scaffold is provided in __initialize_widgets() (DO NOT EDIT).
Step 2: Add Contact event handling (signal/slot) is implemented.
Step 4: Remove Contact event handling (signal/slot + confirmation) is implemented.
Step 5: Test-step fixes:
        - Show a status message when user clicks 'No' in the confirm dialog.
        - Treat 'no selection' correctly by requiring an explicit selection.
        - Clear selection after Add so the 'no selection' test is meaningful.
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
    QMessageBox,  # Confirm remove (Step 4)
)
from PySide6.QtCore import Slot


class ContactList(QMainWindow):
    """
    Provides a UI to manage contacts.

    Notes on steps:
      - Step 1: UI is created in __initialize_widgets() (DO NOT EDIT).
      - Step 2: Private Slot for Add wired to add_button.
      - Step 4: Private Slot for Remove wired to remove_button.
      - Step 5: Cancel confirmation and explicit-selection behavior.
    """

    def __init__(self):
        """Initializes a new instance of the ContactList class."""
        super().__init__()
        self.__initialize_widgets()

        # Step 2: Connect the Add button's clicked signal to the private Slot.
        self.add_button.clicked.connect(self.__on_add_contact)

        # Step 4: Connect the Remove button's clicked signal to the private Slot.
        self.remove_button.clicked.connect(self.__on_remove_contact)

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

            # Ensure nothing appears selected by default.
            self.contact_table.clearSelection()
        else:
            self.status_label.setText("Please enter a contact name and phone number.")

    # -----------------------------
    # Step 4/5: Remove Contact (private Slot)
    # -----------------------------
    @Slot()
    def __on_remove_contact(self):
        """
        Removes the user-selected row after confirmation.

        Behaviour (per Activity Step 4/5):
            - If a row is explicitly selected:
                * Ask: "Are you sure you want to remove the selected contact?"
                * On Yes: remove the row and set status -> "Contact removed."
                * On No:  set status -> "Removal canceled."
            - If no row selected:
                * Set status -> "Please select a row to be removed."
        """
        row = self.contact_table.currentRow()

        # Step 5: Require an explicit selection (protects against implicit 'current row').
        has_explicit_selection = len(self.contact_table.selectedItems()) > 0
        if row < 0 or not has_explicit_selection:
            self.status_label.setText("Please select a row to be removed.")
            return

        reply = QMessageBox.question(
            self,
            "Remove Contact",
            "Are you sure you want to remove the selected contact?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.contact_table.removeRow(row)
            self.status_label.setText("Contact removed.")
        else:
            # Step 5: explicit confirmation when the user cancels.
            self.status_label.setText("Removal canceled.")
