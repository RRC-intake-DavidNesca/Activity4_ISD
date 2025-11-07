"""The module defines the ContactList class.

Activity 4 - Part 1 (Contact List):
- Step 1: UI scaffold created in __initialize_widgets() (DO NOT EDIT).
- Step 2: Add Contact event handling (private Slot) and signal wiring.
- Step 4: Remove Contact event handling (private Slot) with confirmation.
- Step 5: Edits after testing

This window allows users to add and remove contacts using a simple table.
"""

__author__ = "David Nesca"
__version__ = "1"

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
    Notes on steps:
      - Step 1: UI is created in __initialize_widgets() (DO NOT EDIT).
      - Step 2: Private Slot for Add wired to add_button.
      - Step 4: Private Slot for Remove wired to remove_button.
      - Step 5: Cancel confirmation + explicit-selection handling.
    """

    def __init__(self):
        """Initializes a new instance of the ContactList class.

        Wires signals to private Slots:
            - Step 2: add_button.clicked -> __on_add_contact
            - Step 4: remove_button.clicked -> __on_remove_contact
        Returns: None
        """
        super().__init__()
        self.__initialize_widgets()

        # Step 2: Connect the Add button's clicked signal to the private Slot.
        self.add_button.clicked.connect(self.__on_add_contact)

        # Step 4: Connect the Remove button's clicked signal to the private Slot.
        self.remove_button.clicked.connect(self.__on_remove_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.

        Step 1 (given layout – do not edit).
        Returns:
            None
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
        """Step 2: Private slot for Add Contact.

        Reads inputs from QLineEdit widgets, trims whitespace, and:
          - If both fields have data:
                * append a row to the table (Name, Phone)
                * update status -> "Added contact: {name}"
                * clear any selection so a subsequent Remove requires selection
          - Else:
                * update status -> "Please enter a contact name and phone number."
        Returns:
            None
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

            # Step 5: ensure nothing appears selected by default.
            self.contact_table.clearSelection()
        else:
            self.status_label.setText("Please enter a contact name and phone number.")

    # -----------------------------
    # Step 4/5: Remove Contact (private Slot)
    # -----------------------------
    @Slot()
    def __on_remove_contact(self):
        """Step 4/5: Private slot for Remove Contact with confirmation.

        Behavior:
          - Require an explicit selection (selectedItems() must be non-empty).
          - If no selection -> status: "Please select a row to be removed."
          - If selected:
                * QMessageBox.question "Remove Contact" (Yes/No, default No)
                * On Yes -> remove row; status: "Contact removed."
                * On No  -> status: "Removal canceled."
        Returns:
            None
        """
        row = self.contact_table.currentRow()

        # Explicit selection guards against a hidden "current" row still set by Qt
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
            self.status_label.setText("Removal canceled.")
