import csv


class TeamRatings:
    def __init__(self):
        self.teams = {}
        self.load()

    def load(self):
        with open("data/teams.csv", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.teams[row["team"]] = {
                    "conference": row["conference"],
                    "rating": float(row["rating"])
                }