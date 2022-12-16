# This function returns a boolean value that returns of a given 6 digit number is a palindrome or not

def ispalindrome(number):
    first_half = str(number)[:3]
    second_half = str(number)[-3:]
    second_half = second_half[::-1]
    if(first_half == second_half):
        return True
    else:
        return False

 
maximum = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        tempmaximum = i*j
        if ispalindrome(tempmaximum) and tempmaximum > maximum:
            maximum = tempmaximum

print(maximum)






