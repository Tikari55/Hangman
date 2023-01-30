import random
word = random.choice(open("words.txt").read().split())
print(word)

length_of_word = len(word)
initial_output = '_' * length_of_word
print(initial_output)
guesses_left = length_of_word
print("Guesses left:", guesses_left)
for i in range(length_of_word):
    input_char = input("Enter a character:")
    if len(input_char) == 1:
        guesses_left -= 1
        print("Guesses left:", guesses_left)
    else:
        print("You must enter a single character.")

if guesses_left == 0:
    print("You are out of guesses. Game over!")