#**args is used for multiple keyword arguments, like in example
#id, name, and age are keyword arguments and Python 
#authomaticaly packages them into a dictionary
def save_user(**users):
    print(users)


save_user(id=1, name="John", age=22)
save_user(id=2, name="Martha", age=20)
