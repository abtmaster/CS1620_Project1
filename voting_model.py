import csv
import os


def has_voted(voter_id: str, filename: str = "votes.csv") -> bool:
    """
    Check if the voter has already voted
    """
    if not os.path.exists(filename):
        return False
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2 and row[0] == voter_id:
                return True
    return False


def cast_vote(voter_id: str, candidate: str, filename: str = "votes.csv") -> None:
    """
    Record a new vote in the CSV file
    """
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([voter_id, candidate])


def get_vote_counts(filename: str = "votes.csv") -> tuple[int, int]:
    """
    Count the number of votes for John and Jane
    """
    john = 0
    jane = 0
    if os.path.exists(filename):
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    if row[1] == "John":
                        john = john + 1
                    elif row[1] == "Jane":
                        jane = jane + 1
    return john, jane
