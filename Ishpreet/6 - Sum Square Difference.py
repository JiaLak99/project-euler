# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
import math
input_num = int(input("Enter the max number: "))

def sumNatNums(n):
    return n * (n + 1) / 2

def sumSqNatNums(n):
    return n * (n + 1) * (2*n + 1) / 6

print(math.pow(sumNatNums(input_num), 2) - sumSqNatNums(input_num))