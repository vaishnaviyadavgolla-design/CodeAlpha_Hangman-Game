import random


def display_hangman(incorrect_guesses):
    """Return ASCII art of the hangman based on incorrect guesses."""
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[incorrect_guesses]


def get_word():
    """Select a random word from the predefined word list."""
    word_list = ["python", "hangman", "computer", "science", "keyboard"]
    return random.choice(word_list)


def display_word(chosen_word, guessed_letters):
    """Build the display string showing guessed letters and underscores."""
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def is_word_guessed(chosen_word, guessed_letters):
    """Check if all letters in the word have been guessed."""
    for letter in chosen_word:
        if letter not in guessed_letters:
            return False
    return True


def play_hangman():
    """Main function to run the Hangman game."""
    chosen_word = get_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("=" * 45)
    print("       WELCOME TO HANGMAN GAME")
    print("       CodeAlpha Internship Task")
    print("=" * 45)
    print(f"\n  The word has {len(chosen_word)} letters.")
    print(f"  You get {max_incorrect} incorrect guesses.\n")

    # Game Loop
    while incorrect_guesses < max_incorrect:
        # Display hangman ASCII art
        print(display_hangman(incorrect_guesses))

        # Display current word state
        print(f"  Word:    {display_word(chosen_word, guessed_letters)}")
        print(f"  Guesses left: {max_incorrect - incorrect_guesses}")
        print(f"  Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print("-" * 45)

        # Check win condition
        if is_word_guessed(chosen_word, guessed_letters):
            print("\n" + "=" * 45)
            print("  🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"  The word was: {chosen_word.upper()}")
            print("=" * 45)
            return

        # Prompt for input
        guess = input("\n  Enter a letter: ").lower().strip()
        print()

        # Guess Validation (if-else logic)
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠ Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print(f"  ⚠ You already guessed '{guess}'. Try a different letter.")
        elif guess in chosen_word:
            guessed_letters.append(guess)
            print(f"  ✅ Good guess! '{guess}' is in the word.")
        else:
            guessed_letters.append(guess)
            incorrect_guesses += 1
            print(f"  ❌ Wrong! '{guess}' is not in the word.")

    # Loss Condition
    print(display_hangman(incorrect_guesses))
    print("=" * 45)
    print("  💀 GAME OVER! YOU LOST! 💀")
    print(f"  The word was: {chosen_word.upper()}")
    print("=" * 45)


# Run the game
if __name__ == "__main__":
    play_hangman()
