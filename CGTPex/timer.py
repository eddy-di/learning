import time

# Get the duration of the timer from the user
duration = int(input('Enter the duration of the timer in seconds: '))

# Get the current time
start_time = time.time()

# Run the timer
while True:
    # Get the elapsed time
    elapsed_time = time.time() - start_time
    
    # If the elapsed time is greater than the duration, break the loop
    if elapsed_time > duration:
        break
    
    # Print the elapsed time every second
    print(f'Elapsed time: {elapsed_time:.0f} seconds')
    
    # Sleep for 1 second
    time.sleep(1)

print('Timer finished!')
