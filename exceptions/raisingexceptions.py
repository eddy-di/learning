# it is as said in videolesson is a costly practise and its better not to raise exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
# this info i s given to know that some programmers can do like this