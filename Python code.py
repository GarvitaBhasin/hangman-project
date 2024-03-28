
import tkinter as tk
import random
​
class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.config(bg="#FFDAB9") 
​
        self.wordlist = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "kiwi", "pineapple", "blueberry"]  # Add more words
        self.secret_word = random.choice(self.wordlist)
        self.guessed_letters = []
​
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="#FFDAB9") 
        self.canvas.pack()
​
        self.draw_hangman()
​
        self.word_display = tk.Label(self.master, text=self.get_display_word(), font=("Arial", 24), bg="#FFDAB9")  # Set label background color
        self.word_display.pack()
​
        self.keyboard_frame = tk.Frame(self.master, bg="#FFDAB9")  # Set frame background color
        self.keyboard_frame.pack()
​
        self.create_keyboard_buttons()
​
        self.message_label = tk.Label(self.master, text="", font=("Arial", 18), bg="#FFDAB9")  # Set label background color
        self.message_label.pack()
​
        self.time_limit = 30  # Time limit in seconds
        self.time_remaining = self.time_limit
        self.timer_label = tk.Label(self.master, text=f"Time left: {self.time_remaining} seconds", font=("Arial", 12), bg="#FFDAB9")  # Set label background color
        self.timer_label.pack()
​
        self.start_timer()
​
    def draw_hangman(self):
        self.canvas.create_line(150, 350, 300, 350)
        self.canvas.create_line(225, 350, 225, 100)
        self.canvas.create_line(225, 100, 275, 100)
        self.canvas.create_line(275, 100, 275, 130)
​
    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        return display_word
​
    def create_keyboard_buttons(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            button = tk.Button(self.keyboard_frame, text=letter, width=3, height=2, font=("Arial", 12), bg="#ffffff", command=lambda l=letter: self.make_guess(l))  # Increase button size and change font
            button.grid(row=(ord(letter)-ord('a'))//9, column=(ord(letter)-ord('a'))%9, padx=2, pady=2)  # Add padding between buttons
​
    def make_guess(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter not in self.secret_word:
                self.draw_hangman_part()
            self.update_display()
            self.check_game_over()
​
    def draw_hangman_part(self):
        parts = len([letter for letter in self.guessed_letters if letter not in self.secret_word])
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
            self.message_label.config(text="You lost. The word was: " + self.secret_word)
​
    def update_display(self):
        self.word_display.config(text=self.get_display_word())
​
    def check_game_over(self):
        if all(letter in self.guessed_letters for letter in self.secret_word):
            self.message_label.config(text="Congratulations! You won.")
            self.stop_timer()  # Stop the timer when the game is won
​
    def start_timer(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time left: {self.time_remaining} seconds")
            self.timer = self.master.after(1000, self.start_timer)
        else:
            self.message_label.config(text="Time's up!")
            self.stop_timer()  # Stop the timer when time is up
​
    def stop_timer(self):
        if hasattr(self, 'timer'):
            self.master.after_cancel(self.timer)
​
def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
​
if __name__ == "__main__":
    main()
​
