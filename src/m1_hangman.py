"""
Hangman.

Authors: Kirsten Rockey, Jack Wilson.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
import random

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
def word_picker(n):
    #picks work length n or greater
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    #while True:
        while True:
            r = random.randrange(0, len(words))
            if len(words[r]) > n:
                return words[r]


def letter_checker(letter, word):
    index = []
    for i in range(len(word)):
        if letter == word[i]:
            index.append(i)
    if len(index) > 0:
        print('There is a ' + letter + ' in the hidden word.')
    else:
        print('There is not a ' + letter + ' in the hidden word.')
    return index


def string_converter(word_array):
    string = ''
    for j in range(len(word_array)):
        string += word_array[j]
    return string


def game(random_word, picks):
    hidden_word = []
    for i in range(len(random_word)):
        hidden_word.append('_ ')
    # print(random_word)

    while True:
        print('The hidden word is: ', end='')
        print(string_converter(hidden_word))
        guess = str(input('Guess a letter in the word. '))
        index = letter_checker(guess, random_word)
        if len(index) > 0:
            for i in range(len(index)):
                hidden_word[index[i]] = guess
        else:
            picks -= 1
            print('You have ' + str(picks) + ' guesses left!')
        if picks == 0:
            print('The hidden word was ' + random_word)
            return False
        if string_converter(hidden_word) == random_word:
            print('The hidden word was ' + random_word)
            return True


def main():
    while True:
        print('The game has started!')
        min_length = int(input('What is the desired minimum length of the hidden word?: '))
        picks = int(input('How many chances do you want to give yourself? '))
        random_word = word_picker(min_length)
        if game(random_word, picks):
            print('You win!')
        else:
            print('You lost! Sorry!')
        print('The game is over!')
        re = str(input('Do you want to play again? (y/n)'))
        if re == 'n':
            break


main()

####### Do NOT attempt this assignment before class! #######

