import random
import string
from words import words

print(
    """
    Welcome to Hangman the  game!
    The rules are simple, you are given a random word,
    then you have 6 turns to guess which word
    is lurking in the wilderness!
    """
)


def get_valid_word(words):
    """
    Generate valid random words
    """
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def name():
    """
    Asks user to enter name
    """
    while True:
        name = input("What's your name?\n")

        if name.isalpha():
            print(f"Good luck {name}!")
            run_game()
            break
        else:
            print("Not a valid name, please try again")


def run_game():
    """
    Runs the game and enables the player to play again after finished round
    """
    while True:
        print("Do you want to play?")
        run_game = input("Press 'Y' for yes and 'N' for no\n").upper()

        if run_game == "Y":
            play_game()
            break
        elif run_game == "N":
            end_game()
            break
        else:
            print("Invalid input, please choose Y or N")


def end_game():
    """
    Ends game
    """
    print("Thanks for playing, see you next time!")
    exit()


def play_game():
    """
    Runs the game, a random word is chosen and the
     player guesses which letters are in the word
    """
    alpha = set(string.ascii_uppercase)
    word = get_valid_word(words)
    letters_word = set(word)
    secret_word = " _ " * len(word)
    guessed_letters = set()
    turns = 6
    print("Let's start!")
    print(f"Turns left: {turns}")
    print(secret_word)
    while len(letters_word) and turns > 0:
        print(" Guessed letters: ", " ".join(guessed_letters))
        print(f"Turns left: {turns}")
        print(stages_for_hanging(turns))
        guess = input("Pick a letter: \n").upper()

        if guess in alpha - guessed_letters:
            guessed_letters.add(guess)
            if guess in letters_word:
                letters_word.remove(guess)
                print("" "Well done!")
            else:
                turns -= 1
                print(f"{guess} is not in the secret word")
        elif guess in guessed_letters:
            print(f"You already tried {guess} try again")
        else:
            print(f"{guess} is not a valid guess, please choose one letter")

        for letter in word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print(" _ ", end="")

    if turns == 0:
        print(stages_for_hanging(turns))
        print(f" Sorry you lost, the secret word was {word}")
        run_game()
    else:
        print(f" Congratulations! The secret word was {word}")
        run_game()


def stages_for_hanging(turns):
    """
    Displays the different stages for number of turns
    """
    stages = [  # Final stage: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[turns]


name()
run_game()
play_game()
