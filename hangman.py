import random
import string


def get_word():
    word = random.choice(open("words.txt").read().split())
    return word


def hangman():
    current_word = get_word()
    letters_in_word = set(current_word)
    used_letters = set()
    guesses_left = 7

    # user input
    while len(letters_in_word) > 0 and guesses_left > 0:
        print("You have ", guesses_left,  " guesses left and you have used these letters: ", ' '.join(used_letters))

        # showing word and letters
        word_list = [letter if letter in used_letters else '_' for letter in current_word]
        print("Your word: ", ' '.join(word_list))

        input_char = input("Enter a letter: ").lower()
        if input_char in alphabet - used_letters:
            used_letters.add(input_char)
            if input_char in letters_in_word:
                letters_in_word.remove(input_char)
            else:
                print("The letter you guessed is not in the word.")
                guesses_left -= 1
        elif input_char in used_letters:
            print("You have already guessed this letter.")
        else:
            print("The character you entered is not valid.")

        # when no more guesses or all letters guessed
        if guesses_left == 0:
            print("You are out of guesses! The word was:", current_word)
        else:
            print("You guessed the word!")


alphabet = set(string.ascii_lowercase)
hangman()
