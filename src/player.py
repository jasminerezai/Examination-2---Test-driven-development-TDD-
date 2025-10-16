"""
Player class for Pig Dice Game.
Represents a human player and tracks their score.
"""

class Player:
    """A human player with a name and score."""

    def __init__(self, name):
        """Initialize the player with a name and zero score."""
        self.name = name
        self.score = 0

    def add_points(self, points):
        """Add points to the player's score."""
        self.score += points

    def reset_score(self):
        """Reset the player's score to zero."""
        self.score = 0

    def __str__(self):
        """Return a string summary of the player's current score."""
        return f"{self.name}: {self.score} points"
