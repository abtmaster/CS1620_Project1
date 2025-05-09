from PyQt6.QtWidgets import *
from voting_view import *
from voting_model import *


class Controller(QMainWindow, Ui_MainWindowAlexTarasov):
    def __init__(self) -> None:
        """
        Initialize the voting application GUI
        """
        super().__init__()
        self.setupUi(self)
        self.SubmitButton.clicked.connect(self.handle_vote)
        self.update_vote_counts()

    def handle_vote(self) -> None:
        """
        Handle vote submission when button is clicked
        """
        voter_id = self.VoterID.text().strip()
        candidate = None

        if self.JohnRadioButton.isChecked():
            candidate = "John"
        elif self.JaneRadioButton.isChecked():
            candidate = "Jane"

        if voter_id == "":
            self.show_status("Voter ID is required", "red")
            return

        if not candidate:
            self.show_status("Please select a candidate", "red")
            return

        if has_voted(voter_id):
            self.show_status("Cannot vote multiple times", "red")
            return

        try:
            cast_vote(voter_id, candidate)
            self.show_status("Vote submitted", "green")
            self.VoterID.clear()
            self.JohnRadioButton.setAutoExclusive(False)
            self.JohnRadioButton.setChecked(False)
            self.JohnRadioButton.setAutoExclusive(True)
            self.JaneRadioButton.setAutoExclusive(False)
            self.JaneRadioButton.setChecked(False)
            self.JaneRadioButton.setAutoExclusive(True)
            self.update_vote_counts()
        except Exception:
            self.show_status("Error saving vote", "red")

    def show_status(self, message: str, color: str) -> None:
        """
        Show status message to the user
        """
        self.StatusMessage.setStyleSheet("color: " + color + ";")
        self.StatusMessage.setText(message)

    def update_vote_counts(self) -> None:
        """
        Update vote count label based on current vote data
        """
        john, jane = get_vote_counts()
        self.voteCountLabel.setText("John: " + str(john) + " votes, Jane: " + str(jane) + " votes")
