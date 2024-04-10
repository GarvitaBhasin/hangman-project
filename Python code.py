import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.config(bg="#FFDAB9") 

        # Add game name label
        self.game_name_label = tk.Label(self.master, text=" WORD WACKY", font=("Arial", 13), bg="#FFDAB9")
        self.game_name_label.pack()

        self.word_categories = {
            "Fruits": ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "kiwi", "pineapple", "blueberry"],
            "Animals": ["dog", "cat", "elephant", "lion", "tiger", "giraffe", "zebra", "monkey", "penguin"]
        }

        self.category = random.choice(list(self.word_categories.keys()))
        self.secret_word = random.choice(self.word_categories[self.category])
        self.guessed_letters = []
        self.lives = 6  # Number of lives

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="#FFDAB9") 
        self.canvas.pack()

        self.draw_hangman()

        self.word_display = tk.Label(self.master, text=self.get_display_word(), font=("Arial", 24), bg="#FFDAB9") 
        self.word_display.pack()

        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.lives}", font=("Arial", 12), bg="#FFDAB9") 
        self.attempts_label.pack(side="right", padx=10, pady=10)

        self.keyboard_frame = tk.Frame(self.master, bg="#FFDAB9") 
        self.keyboard_frame.pack()

        self.create_keyboard_buttons()

        self.message_label = tk.Label(self.master, text="", font=("Arial", 18), bg="#FFDAB9") 
        self.message_label.pack()

        self.time_limit = 30  
        self.time_remaining = self.time_limit
        self.timer_label = tk.Label(self.master, text=f"Time left: {self.time_remaining} seconds", font=("Arial", 12), bg="#FFDAB9") 
        self.timer_label.pack()

        self.start_timer()

    def draw_hangman(self):
        self.canvas.create_line(150, 350, 300, 350)
        self.canvas.create_line(225, 350, 225, 100)
        self.canvas.create_line(225, 100, 275, 100)
        self.canvas.create_line(275, 100, 275, 130)

    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        return display_word

    def create_keyboard_buttons(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            button = tk.Button(self.keyboard_frame, text=letter, width=3, height=2, font=("Arial", 12), bg="#ffffff", command=lambda l=letter: self.make_guess(l))
            button.grid(row=(ord(letter)-ord('a'))//9, column=(ord(letter)-ord('a'))%9, padx=2, pady=2)

    def make_guess(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter not in self.secret_word:
                self.lives -= 1
                self.draw_hangman_part()
            self.update_display()
            self.update_attempts()
            self.check_game_over()

    def draw_hangman_part(self):
        parts = 6 - self.lives
        if parts == 1:
            self.canvas.create_oval(250, 130, 300, 180)
        elif parts == 2:
            self.canvas.create_line(275, 180, 275, 250)
        elif parts == 3:
            self.canvas.create_line(275, 200, 250, 225)
        elif parts == 4:
            self.canvas.create_line(275, 200, 300, 225)
        elif parts == 5:
            self.canvas.create_line(275, 250, 250, 275)
        elif parts == 6:
            self.canvas.create_line(275, 250, 300, 275)
            self.message_label.config(text=f"You lost. The word was: {self.secret_word}")

    def update_display(self):
        self.word_display.config(text=self.get_display_word())

    def update_attempts(self):
        self.attempts_label.config(text=f"Attempts left: {self.lives}")

    def check_game_over(self):
        if self.lives == 0:
            self.message_label.config(text=f"You ran out of lives. The word was: {self.secret_word}")
            self.stop_timer()
        elif all(letter in self.guessed_letters for letter in self.secret_word):
            self.message_label.config(text="Congratulations! You won.")
            self.stop_timer()

    def start_timer(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time left: {self.time_remaining} seconds")
            self.timer = self.master.after(1000, self.start_timer)
        else:
            self.message_label.config(text="Time's up!")
            self.stop_timer()

    def stop_timer(self):
        if hasattr(self, 'timer'):
            self.master.after_cancel(self.timer)

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
