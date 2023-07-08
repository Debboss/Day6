from tkinter import Tk, Label, Entry, Button, messagebox, LabelFrame
from faker import Faker
import time

root = Tk()
root.title("Hangman Game")

guess_letter = []

def loading_bar():
    loading_label.config(text="Wait until we find the word for you... ")
    loading_label.update()
    
    for _ in range(10):
        loading_label.config(text=loading_label.cget("text"))
        loading_label.update()
        time.sleep(0.3)
    
    loading_label.config(text=loading_label.cget("text") + " \nComplete!")

def start_game(event=None):
    start = start_entry.get().lower()
    
    if start in ['s', 'start']:
        loading_bar()
        game_frame()
    elif start in ['q', 'quit']:
        messagebox.showinfo("Hangman Game", "You are exiting from the game...")
        root.destroy()
    else:
        messagebox.showerror("Hangman Game", "Invalid input. Try again or press 'q' to quit.")

def game_frame():
    start_button.destroy()  # Remove the Start button
    
    game_frame = LabelFrame(root, text="Hangman Game")
    game_frame.pack(padx=20, pady=10)
    
    fake = Faker()
    random_word = fake.word().lower()
    
    Label(game_frame, text="The word you need to guess is the following: ").pack(pady=10)
    
    hidden_word = ['_' if c.isalpha() else ' ' for c in random_word]
    word_label = Label(game_frame, text=' '.join(hidden_word))
    word_label.pack(pady=10)
    
    correct_guesses = []
    
    def check_guess(event=None):
        letter = letter_entry.get().lower()
        
        if letter in correct_guesses:
            messagebox.showwarning("Hangman Game", f"You already guessed the letter '{letter}'. Try again!")
            letter_entry.delete(0, 'end')
            return
        
        if letter in random_word:
            # Update the hidden_word with the correctly guessed letter(s)
            for i, c in enumerate(random_word):
                if c == letter:
                    hidden_word[i] = letter
                    word_label.config(text=' '.join(hidden_word))
            
            correct_guesses.append(letter)
            
            if '_' not in hidden_word:
                messagebox.showinfo("Hangman Game", "Congratulations! You guessed the word correctly.")
                root.destroy()
        else:
            messagebox.showwarning("Hangman Game", f"The letter '{letter}' is not in the hidden word. Try again!")
        
        letter_entry.delete(0, 'end')
    
    letter_entry = Entry(game_frame)
    letter_entry.pack(pady=10)
    letter_entry.focus()
    letter_entry.bind('<Return>', check_guess)  # Bind Return key event
    
    check_button = Button(game_frame, text="Check", command=check_guess)
    check_button.pack(pady=10)

start_label = Label(root, text="Welcome to Hangman!")
start_label.pack(padx=20, pady=10)

start_entry = Entry(root)
start_entry.pack(pady=10)
start_entry.focus()
start_entry.bind('<Return>', start_game)  # Bind Return key event

start_button = Button(root, text="Start", command=start_game)
start_button.pack(pady=10)

loading_label = Label(root, text="")
loading_label.pack()

root.mainloop()
