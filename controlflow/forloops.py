successful = True
for number in range(2, 20, 2):
    print("Attempt", number, number * ".")
    if successful:
        print("Successful")
        break
