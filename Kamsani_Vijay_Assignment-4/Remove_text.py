"""
HW 4
Problem 1
Author: Vijay Kumar Kamsani
"""

import os
import re

# main function to run the program
if __name__ == '__main__':
    try:
        # Enter the file name
        file = input("Enter a filename: ")
        # Enter the string that needs to remove
        remove_string = input("Enter the string to be removed: ")
        text_file = open(file, 'r')
        temp_file = open('temp_file.txt', 'w')
        with text_file, temp_file:
            # Using the loop function we are splitting the data
            for line in text_file:
                words = line.split()
                for word in words:
                    if word.lower() != remove_string.lower():
                        temp_file.write(word + ' ')
                temp_file.write('\n')
        os.remove(file)
        os.replace('temp_file.txt', file)
        print("Done")
    except FileNotFoundError as e:
        print(e)
