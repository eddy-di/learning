x = input("Outside temperature: ")
temperature = int(x)
if temperature >= 35 or temperature > 40:
    print("It's hot")
    print("Stay hydrated")
elif temperature >= 17 or temperature <= 34:
    print("It's nice")
elif temperature >= 5 or temperature <= 16:
    print("Put on some light coat")
else:
    print("It's cold")
    print("Dress warmly")
print("Weather check executed!")
