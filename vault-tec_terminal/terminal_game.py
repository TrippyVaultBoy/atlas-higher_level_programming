import random

class Terminal_game():
    def __init__(self, words, max_attempts=4):
        self.words = words
        self.correct_word = random.choice(words)
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts

    def display_words(self):
        print("Choose correct password:")
        for word in self.words:
            print(word, "- ", end="")
        print()

    def play(self):
        while self.attempts_left > 0:
            self.display_words()
            guess = input("Enter your guess: ").strip().lower()
            if guess == self.correct_word:
                print("Correct password!")
                return True
            else:
                self.attempts_left -= 1
                print("Incorrect! Attempts left: ", self.attempts_left)
        
        print("Out of attempts! Correct password: ", self.correct_word)
        return False
