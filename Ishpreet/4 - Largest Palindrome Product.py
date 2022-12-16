# Find the largest palindrome made from the product of two 3-digit numbers
start = int(input("Enter starting number for palindrome finder: "))
end = int(input("Enter ending number for palindrome finder: "))

# reverses input using mod 10 and returns whether the input is a palindrome
def isPalindrome(n):
    straight = n
    flipped = 0
    while n >= 1:
        flipped = 10 * flipped + n % 10
        n = n // 10
    return straight == flipped

largestPalindrome = 0
while end >= start:
    num2 = end
    while num2 >= start:
        attNum = end * num2
        # no point in checking if the number isn't the largest palindrome
        if attNum < largestPalindrome:
            break
        if isPalindrome(attNum) and attNum > largestPalindrome:
            largestPalindrome = attNum
        num2 = num2 - 1
    end = end - 1

print(largestPalindrome)