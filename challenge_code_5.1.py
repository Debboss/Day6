from faker import Faker
import time

guess_letter = [];

def loading_bar():
    print("Wait until we find the word for you... ", end="")
    
    for _ in range(10):
        print("■", end="", flush=True)
        time.sleep(0.3)
    
    print(" \nComplete!")

print("Welcome to Hangman!")

while True:
    start = input("Press 's' to start or 'q' to quit: ")

    if start.lower() in ['s', 'start']:
        loading_bar();
        break
    elif start.lower() in ['q', 'quit']:
        print("You are exiting from the game...")
        exit()
    else:
        print("This is not a valid input. Try again or press 'q' to quit.")


from faker import Faker

fake = Faker()
random_word = fake.word().lower()

print("The word you need to guess is the following: ")

hidden_word = ['_' if c.isalpha() else ' ' for c in random_word]

print(' '.join(hidden_word))

correct_guesses = []

while True:
    letter = input("Guess a letter: ").lower()

    if letter in correct_guesses:
        print(f"You already guessed the letter '{letter}'. Try again!")
        continue

    if letter in random_word:
        # Update the hidden_word with the correctly guessed letter(s)
        for i, c in enumerate(random_word):
            if c == letter:
                hidden_word[i] = letter

        correct_guesses.append(letter)

        print(f"The letter '{letter}' is in the hidden word")
        print(' '.join(hidden_word))

        if '_' not in hidden_word:
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        print(f"The letter '{letter}' is not in the hidden word. Try again!")

