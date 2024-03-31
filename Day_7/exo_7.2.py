#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')


guess = input("Guess a letter: ").lower()


display = ["_" for _ in range(len(chosen_word))]
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess


print(display)