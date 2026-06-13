#TODO-1 - Randomly choose a word from the word list and assign it to a variable called chosen word. Then print it.
import random

word_list = ["bird", "flower", "vegetable", "medicine"]
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_word = input("Please guess a word: ").lower()
print(guess_word)

#TODO-3 - Check if the letter the user guessed is one of the letters in the chosen words, print right if it is, print wrong if it is not.
for letter in chosen_word:
    if guess_word == letter:
        print("Right")
    else:
        print("Wrong")

#TODO-4 - Create a placeholder with the same number of blanks as the chosen word.
placeholder = ""

length = len(chosen_word)

for position in range(length):
    placeholder += "_"

print(placeholder)