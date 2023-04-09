import sys

if len(sys.argv) == 1:
    print("USAGE: python dices.py <password>")
else:
    password = sys.argv[1]
    print("Password is set to:", password)