# Find the sum of all the multiples of 3 or 5 below 1000.

starting_number = int(input("Give the starting number."))
ending_number = int(input("Give the ending number."))

sum = 0
for i in range(starting_number, ending_number):
    if (i % 3 == 0 or i % 5 == 0):
        sum = sum + i
print(sum)
