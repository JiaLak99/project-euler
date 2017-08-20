starting_number = input("Give the starting number. ")
ending_number = input("Give the ending number. ")

sum = 0
for i in range(starting_number, ending_number):
    if (i % 3 == 0 or i % 5 == 0):
        sum = sum + i
print sum
