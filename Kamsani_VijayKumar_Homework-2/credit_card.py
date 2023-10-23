"""
Homework 2
Problem 2
Vijay kumar kamsani
"""


def check_even_digits(c):  # function to validate the credit card for second digit from right to left
    even_digits = [int(i) * 2 % 10 + int(i) * 2 // 10 if int(i) * 2 >= 10 else int(i) * 2
                   for i in c[-2::-2]]  # list comprehension to get the even place digits
    return sum(even_digits)


def check_odd_digits(c):
    odd_digits = [int(i) for i in c[-1::-2]]  # list comprehension to get the odd place digits
    return sum(odd_digits)


if __name__ == '__main__':

    while True:
        card = input("Please enter your credit card number: ")  # prompt user to enter a credit card number
        if (13 <= len(card) <= 16) and card.startswith(
                ('4', '5', '37', '6')):  # validity check for different business cards
            break
        else:
            print("Your card is too short and/or does not belong to a company")
    if (check_even_digits(card) + check_odd_digits(card)) % 10 == 0:
        print(card, " is valid card")
    else:
        print(card, " is not a valid card")
