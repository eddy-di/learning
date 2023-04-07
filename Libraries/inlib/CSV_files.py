import csv

# with open("data.csv", "w") as file: # this is a way of opening/creating csv file if not included, and "w" allows to write in it
#     writer = csv.writer(file) # making an object with csv.writer method
#     writer.writerow(["transaction_id", "product_id", "price"]) # adding row 1
#     writer.writerow([1000, 1, 5]) # adding row 2
#     writer.writerow([1001, 2, 10]) # adding row 3
# aforewritten lines of code give possibility to open, create and write data to csv files

with open("data.csv") as file:
    reader = csv.reader(file) # allows to read created file in lines from 3 to 7
    # print(list(reader)) # gives a result of the rows in list format
    for row in reader:
        print(row)
    