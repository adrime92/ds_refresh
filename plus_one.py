'''You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered 
from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.'''


def plusOne(digits):
    num = None
    digitsArr = []

    # concatenate digits into an integer
    for i in range(len(digits)):
        if num == None:
            num = digits[i]
        else:
            num = str(num) + str(digits[i])
    
    # increment by 1 
    num = int(num)
    num += 1 

    # back to array
    num = str(num)
    print(num)
    
    for i in range(len(num)):
        digitsArr.append(int(num[i]))
    
    print(digitsArr)
    return digitsArr

plusOne([4,3,2,1])
