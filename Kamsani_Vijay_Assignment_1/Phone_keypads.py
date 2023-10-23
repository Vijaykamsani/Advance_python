"""
homework-1
Problem -3
Kamsani vijay kumar
"""


def getNumber(UpperCaseLetter):
    result = ""
    for character in UpperCaseLetter:  # condition to check the user input is  alphanumeric
        if not character.isalpha():
            result += character
        else:  # condition to convert the character to digit
            if character in "ABCabc":
                result += "2"
            elif character in "DEFdef":
                result += "3"
            elif character in "GHIghi":
                result += "4"
            elif character in "JKLjkl":
                result += "5"
            elif character in "MNOmno":
                result += "6"
            elif character in "PQRSpqrs":
                result += "7"
            elif character in "tuvTUV":
                result += "8"
            elif character in "wxyzWXYZ":
                result += "9"
    return result


if __name__ == '__main__':
    number = input("Enter the string:")
    res = getNumber(number)
    print(res)
