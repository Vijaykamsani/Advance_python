"""
HW 4
Problem 2
Author: Vijay Kumar Kamsani
"""

# main function to run the program
if __name__ == '__main__':
    try:
        # Enter the filename
        file_name = input("Enter a filename: ")

        # Read the filename
        file = open(file_name, 'r')
        para = file.read()

        # Counting the number of paragraphs
        count_characters = len(para)

        # Counting the number of words
        count_words = len(para.split())

        # counting the number of lines
        count_lines = len(para.splitlines())

        print(str(count_characters) + " characters")
        print(str(count_words) + " words")
        print(str(count_lines) + " lines")

    except FileNotFoundError as f:
        print(f)
