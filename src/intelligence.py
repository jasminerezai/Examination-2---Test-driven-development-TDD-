import random

class Intelligence:
    """Computer player AI for Pig Dice Game (easy or hard difficulty)."""

    def __init__(self, difficulty='easy'):
        """Initialize computer player with difficulty ('easy' or 'hard')."""
        difficulty = difficulty.lower()
        if difficulty not in ['easy', 'hard']:
            raise ValueError('Difficulty must be "easy" or "hard".')
        self.name = 'Computer Agnetha'
        self.score = 0
        self.difficulty = difficulty.lower()

    def add_points(self, points):
        """Add points to the computer's score."""
        self.score += points

    def reset_score(self):
        """Reset the computer's score to zero."""
        self.score = 0

    def should_hold(self, turn_total, opponent_score):
        """Decide whether to hold based on difficulty and scores."""
        if self.difficulty == 'easy':
            return turn_total >= 10 or random.random() < 0.1
        elif self.difficulty == 'hard':
            if self.score + turn_total >= 100:
                return True
            elif self.score < opponent_score and turn_total >= 15:
                return True
            elif turn_total >= 20:
                return True
            else: 
                return False
