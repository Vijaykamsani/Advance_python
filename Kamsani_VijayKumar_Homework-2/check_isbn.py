"""
homework-2
Problem -1
 vijay kumar Kamsani
"""

# function to check the conditions
def sum_of_isbn(num):
    j = 9
    s = 0
    # using for loop for checking each string and multiplying the number
    for i in range(1, 10):
        # to check the last digit of number
        n = int(num[len(num) - i])
        mul = (n * j)
        s += mul
        j -= 1
    val = s % 11

    # checking if value is 10 then replace it as x keyword
    if val == 10:
        return "X"
    else:
        return val


# main function for user input
if __name__ == '__main__':
    isbn = input("Enter the first 9 digit of an ISBN as a string: ")
    # to add total number word  value as string
    isbn += str(sum_of_isbn(isbn))
    print("The ISBN-10 number is :", isbn)
