successful = False
for number in range(1, 4):
    print("Attempt", number)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")