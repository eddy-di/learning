import time

# Get the number of seconds from the user
seconds = int(input("Enter the number of seconds for the timer: "))

# Calculate the number of minutes and seconds
minutes, seconds = divmod(seconds, 60)

# Countdown from the number of minutes and seconds
while minutes > 0 or seconds > 0:
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
    seconds -= 1
    if seconds < 0:
        minutes -= 1
        seconds = 59

# Timer has reached zero
print("Time's up!")
