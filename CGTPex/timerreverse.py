import time

# Get the number of seconds from the user
seconds = int(input("Enter the number of seconds for the timer: "))

# Countdown from the number of seconds
while seconds > 0:
    print(seconds)
    seconds -= 1
    time.sleep(1)

# Timer has reached zero
print("Time's up!")