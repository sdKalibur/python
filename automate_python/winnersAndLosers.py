#!/bin/python3

import random

def get_random_word():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0, len(words)-1)]
    return word
    # len(words)-1 counts the number of items in the list
    # the -1 ensures its machine readable i,e 0-3 thus 1-4

def show_word(word):
    for character in word:
        print(character, " ",end="")
    print("")

    # the end="" defines how the print should end.  by default the new line char is used
    # but by using end="" we are saying dont print any char after print no new line no nada!
def show_word():
    for character in word:
        print(character, " ", end="")
    print("")


def get_guess():
    print("Enter a Letter: ")
    return input()


def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True
    words = get_random_word()
    blanked_word = "_" * len(word)
    return word



    while playing:
        show_word(blanked_word)
        letter = get_guess()
        
        strikes += 1

        if strikes >= max_strikes:
            play = False


    if strikes >= max_strikes:
        print("Loser!")
    else:
        print("Winner")



print("Game started")

#play_word_game()

print("Game over")
