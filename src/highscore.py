# highscore.py
import json
import os

width = 53
class HighScore:
    FILE_PATH = "highscores.json"

    def __init__(self):
        self.scores = []  # list of dicts: {"name": ..., "score": ...}
        self.load()

    def add_score(self, name, score):
        """Add a new score and save it."""
        self.scores.append({"name": name, "score": score})
        self.save()

    def get_highest(self):
        """Return the entry with the highest score."""
        if not self.scores:
            return None
        return max(self.scores, key=lambda x: x["score"])

    def display_all(self):
        highest = max(self.scores, key=lambda x: x["score"]) if self.scores else None
        width = self.game.width if hasattr(self, "game") else 53  # fallback

        print("\n╔" + "═" * (width - 2) + "╗")
        print("║" + " " * (width - 2) + "║")
        print("║" + "🏆 All-time Scores 🏆".center(width - 4) + "║")
        print("║" + " " * (width - 2) + "║")

        # print each score line nicely centered
        if self.scores:
            for entry in sorted(self.scores, key=lambda x: x["score"], reverse=True):
                line = f"{entry['name']}: {entry['score']}"
                if highest and entry == highest:
                    line += "  <- Highest!"
                print("║" + line.center(width - 2) + "║")
        else:
            print("║" + "No scores yet!".center(width - 2) + "║")

        print("║" + " " * (width - 2) + "║")
        print("╚" + "═" * (width - 2) + "╝")
    
    def save(self):
        """Save scores to a file."""
        try:
            with open(self.FILE_PATH, "w") as f:
                json.dump(self.scores, f)
        except OSError:
            print("Error: Could not save highscores.")

    def load(self):
        """Load scores from a file."""
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, "r") as f:
                    self.scores = json.load(f)
            except (OSError, json.JSONDecodeError):
                self.scores = []
