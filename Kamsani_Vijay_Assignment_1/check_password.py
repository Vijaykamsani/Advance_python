"""
homework-1
Problem -1
Kamsani vijay kumar
"""


def password_check(pwd):
    if len(pwd) < 8:  # checking the length of the password
        return False
    elif not pwd.isalnum():  # checking the pwd as alphanumeric
        return False
    elif not at_least_digits(pwd):
        return False
    else:
        return True


# function to check the pwd contains at least 2 digit
def at_least_digits(d):
    count = 0
    for i in d:
        if i.isdigit():
            count += 1

    if count < 2:
        return False
    else:
        return True


if __name__ == '__main__':
    password = input("enter the password")
    if password_check(password):
        print("is valid password ")
    else:
        print("is not valid password")
