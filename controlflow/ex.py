# need to have an output where the range starts from 2 until 8
# and at the end it will get str "We have 4 even numbers"
count = 0
for number in range(2, 9, 2):
    print(number)
    count += 1 # count = count + 1

print(f"We have {count} even numbers")

for number in range (1, 10, 2):
    print(number)

for number in range (0, 10):
    number_type = "odd"
    if number % 2 == 0:
        number_type = "even"
    print(f"{number} is {number_type}")