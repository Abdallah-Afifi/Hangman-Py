import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "keyboard", "developer", "software", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")

    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 6  # You can adjust the number of attempts as needed

    while True:
        print("\n" + display_word(secret_word, guessed_letters))
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts_left -= 1
            print(f"Oops! '{guess}' is not in the word.")

        if "_" not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You guessed the word: " + secret_word)
            break

        if attempts_left == 0:
            print("\nGame over! The word was: " + secret_word)
            break

if __name__ == "__main__":
    hangman()
