
word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

guess = input("Guest a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
