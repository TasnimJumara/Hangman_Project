#TODO-1 - Randomly choose a word from the word list and assign it to a variable called chosen word. Then print it.
import random

word_list = ["bird", "flower", "vegetable", "medicine"]
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-4 - Create a placeholder with the same number of blanks as the chosen word.
placeholder = ""

length = len(chosen_word)

for position in range(length):
    placeholder += "_"

print(placeholder)

#TODO- 5 - Use a while loop to let the user guess again.
game_over = False
correct_word = []

while not game_over:
    guess_word = input("Please guess a word: ").lower()

    #TODO- 6 - Create a display that puts the guess letter in the right position and a blank in the rest of the string.
    display = ""
    #TODO- 7 - Change the for loop so that you can keep the previous correct letters in the display.
    for letter in chosen_word:
        if guess_word == letter:
            display += guess_word
            correct_word.append(guess_word)
        elif letter in correct_word:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You have won.")