# First case shows the ability to add only two variables in multiply function
def multiply(x, y):
    return x*y


multiply(2, 3)  # we cannot add more variables to function multiply

# Second case is use of *args where lots of variables can be inserted


def m_multiply(*numbers):  # *numbers is *args example and shows the
    # possibilty to include lots of variables for m_multiply
    total = 1  # results are stored here
    for number in numbers:  # results in total are iterated with all available numbers
        total *= number
    return total


print(m_multiply(3, 4, 5, 6, 7))
