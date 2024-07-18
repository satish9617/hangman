import random

# Visual representation of the hangman
HANGMAN_PICS = [
    """
     ------
     |    |
     |
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
     |
    --------
    """
]

# Function to get a random word
def get_random_word(word_list):
    return random.choice(word_list).lower()

# Function to display the current state of the game
def display_game_state(hangman_pics, wrong_guesses, correct_guesses, secret_word):
    print(hangman_pics[len(wrong_guesses)])
    print("\nWrong guesses: ", " ".join(wrong_guesses))
    blanks = "_" * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_guesses:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    print("Word: ", " ".join(blanks))

# Function to get the player's guess
def get_player_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        else:
            return guess

# Function to check if the player has won
def check_win(secret_word, correct_guesses):
    for letter in secret_word:
        if letter not in correct_guesses:
            return False
    return True

# Main function to play the game
def play_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    secret_word = get_random_word(word_list)
    wrong_guesses = []
    correct_guesses = []
    game_over = False

    while not game_over:
        display_game_state(HANGMAN_PICS, wrong_guesses, correct_guesses, secret_word)
        guess = get_player_guess(wrong_guesses + correct_guesses)

        if guess in secret_word:
            correct_guesses.append(guess)
            if check_win(secret_word, correct_guesses):
                print(f"Congratulations! You've guessed the word: {secret_word}")
                game_over = True
        else:
            wrong_guesses.append(guess)
            if len(wrong_guesses) == len(HANGMAN_PICS) - 1:
                display_game_state(HANGMAN_PICS, wrong_guesses, correct_guesses, secret_word)
                print(f"You've run out of guesses. The word was: {secret_word}")
                game_over = True

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()

if __name__ == "__main__":
    play_game()
