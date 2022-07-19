import random
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
    word = random.choice(words)
    while "-" in word or " " in word: 
        word = random.choice(words)

        return word.upper()

def name():
    """
    Askes user to enter his/her name
    """
    while True:
        name = input("What's your name?\n")

    if name.isalpha():
        print(f"Best of luck {name}!")
        run_game()
        break
       
    else:
            print("Not a valid name, please try again")

       