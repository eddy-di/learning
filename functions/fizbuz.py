def fizz_buzz(input):
    case_fizz_buzz = ()
    if input % 3 == 0 and input % 5 == 0:
        return "fizz buzz"
    case_fizz = ()
    if input % 3 == 0:
        return "fizz"
    case_buzz = ()
    if input % 5 == 0:
        return "buzz"
    else:
        return input
    

print(fizz_buzz(17))
