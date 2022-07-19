import random
from words import words

#will generate valid random words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word: 
        word = random.choice(words)

        return word.upper

       