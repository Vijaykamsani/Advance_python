"""
homework-2
Problem -3
vijay kumar Kamsani
"""
# importing random library
import random

if __name__ == '__main__':

    words = ["vijay", "kumar", "dileep", "lalith", "aman"]
    user_input = 'y'
    while user_input == 'y':
        # choosing random word as symbol
        word = random.choice(words)
        hidden_word = str('*' * len(word))
        list1 = '*' * len(word)
        misses = 0
        # while loop checking the * symbol for every word
        while '*' in hidden_word:
            letter = input("Please enter a letter in word {}".format(str(hidden_word)))
            if letter in word and letter in hidden_word:
                print(letter, " is already in the word")
            elif letter in word:
                hidden_word_list = [letter if letter == i else '*' for i in word]
                list1 = [list1[i] if list1[i].isalpha() else hidden_word_list[i] for i in
                         range(0, len(hidden_word_list))]
                hidden_word = ''.join(list1)
            else:
                misses += 1
                print(letter, " is not in the word")
        print("The word is ", word, ". You missed ", misses, " time")
        user_input = input("Do you want to guess another word? Enter y or n")
