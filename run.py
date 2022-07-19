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

def run_game():

    while True:
        print("Do you want to play??")
        run_game = input("Press 'Y' yes and 'N' for no\n").upper()

        if  run_game == "Y":
            play_game()
            break
        elif run_game == "N":
            end_game()
            break
        
        else:
            print("Invalid input, please decided 'Y' or 'N'")

def end_game():
    """
    Game Ends
    """
    print("Thanks for playing, see you next time!")
    
    exit()            

    




       