#! /bin/python3

# words = ["pizza", "cheese", "apples" , "kittens" ]

def get_random_word():
    words = ["pizza", "cheese", "apples" , "kittens" ]
    word = words[random.randint(0, len(words)-1]
    return word
def show_word():
    for character in word:
         print(character, " ", end="")
    print("")

def get_guess():
    print("Enter a letter")
    return input()

def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True
    word = get_random_word()
    blanked_word = "_" * len(word)

    while playing:
        show_word(blanked_word)
        letter = get_guess()

        strikes +=1

        if strikes >= max_strikes:
            playing = False

        if strikes >= max_strikes:
            print("Loser!")

        else:
            print("Winner!")


print("Game Started")

play_word_game()

print("Game Over!")
