a = 2
number = input("Find the largest prime factor of ")

while a * a < number1:
    while number % a == 0:
        number = number / a
    a = a + 1
print number

# code does not work for perfect squares
