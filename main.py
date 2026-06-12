# TODO-1 - Randomly choose a word from the word list and assign it to a variable called chosen word. Then print it.
import random

word_list = ["elephant", "Tiger", "Succinct"]

'''chosen_word = random.choice(word_list)
print(chosen_word)'''

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_word = input("Guess a letter: ").lower()
#print(guess_word)

# TODO-3 - Check if the letter the user guessed is one of the letters in the chosen words, print right if it is print wrong if it is not.
'''for letter in chosen_word:
    if guess_word == letter:
        print("Right")
    else:
        print("Wrong")'''

#TODO-4 - Create a placeholder with the same number of blanks as the chosen word.
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""

length = len(chosen_word)

for position in range(length):
    placeholder += "_"

print(placeholder)

#TODO- 5 - Create a display that puts the guess letter in the right position and a blank in the rest of the string
display = ""

for letter in chosen_word:
    if guess_word == letter:
        display += letter
    else:
        display += "_"

print(display)

#TODO- 6 - Use a while loop to let the user guess again
while len(guess_word) != length:
    guess_word = input("Guess a letter: ").lower()

#TODO- 7 - Change the for loop so that you keep the previous correct letters in display