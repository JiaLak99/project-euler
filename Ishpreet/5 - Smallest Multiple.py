# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
import math
input_num = int(input("Enter the max number: "))

# use the Sieve of Eratosthenes to generate a list of primes
def sieveEratosthenes(n):
    num_array = [1 for i in range(n)]
    num_array[0] = 0
    i = 2
    while i <= math.sqrt(n):
        if num_array[i-1]:
            j = int(math.pow(i, 2))
            while j <= n:
                num_array[j-1] = 0
                j = j + i
        i = i + 1
    return(num_array)

primes = sieveEratosthenes(input_num)
answer = 1

for num in range(1, len(primes)):
    if primes[num - 1]:
        power = math.log(input_num) // math.log(num)
        answer = answer * int(math.pow(num, power))
print(answer)