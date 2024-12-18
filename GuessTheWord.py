import random

class GuessTheWord:
    def __init__(self):
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.target_word = ''
        self.guessed_letters = set()
        self.remaining_attempts = 6

    def start_game(self):
        print("Välkommen till Gissa Ordet")
        self.target_word = random.choice(self.words)
        self.play()

    def display_word(self):
        display = ''.join([])