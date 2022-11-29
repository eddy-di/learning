x = input("Outside temperature: ")
temperature = int(x)
if temperature > 40:
    print("It's hot")
    print("Don't forget to drink some water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
    print("Dress warmly")
print("Weather check executed!")
