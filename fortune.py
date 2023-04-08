num = int(input())
if num < 0 or num >= 37:
    print("error")
elif num == 0:
    print("green")
elif 1 <= num <= 10 and num % 2 == 0:
    print("black")
elif 1 <= num <= 10 and num % 2 != 0:
    print("red")
elif 11 <= num <= 18 and num % 2 != 0:
    print("black")
elif 11 <= num <= 18 and num % 2 == 0:
    print("red")
elif 19 <= num <= 28 and num % 2 == 0:
    print("black")
elif 19 <= num <= 28 and num % 2 != 0:
    print("red")
elif 29 <= num <= 36 and num % 2 != 0:
    print("red")
elif 29 <= num <= 36 and num % 2 == 0:
    print("red")