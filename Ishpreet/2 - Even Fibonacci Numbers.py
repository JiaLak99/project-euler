# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a = 1
b = 2
sum = 0

while (b < 4000000):
    c = a + b
    if (c % 2 == 0):
        sum = sum + c
    a = b
    b = c
print(sum + 2)
