import time
# line1 code imports the possibility to work with time module

def send_emails():
    counter = 0
    for i in range(10000):
        counter += i

start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)