'''You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much
as every other number in the array. If it is, return the index of the largest
element, or return -1 otherwise.

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
'''


def dominantIndex(nums):
    index = 0
    biggest = 0
    ## find the biggest unique integer
    for i in range(len(nums)):
        if nums[i] > biggest:
            biggest = nums[i]
            index = i

    half = int(biggest/2)
    
    ## check if any of the numbers is less than the biggest unique integer / 2
    for i in range(len(nums)):
        if i == index:
            continue
        if nums[i] > half:
            return -1
    
    print(index)
    return index

if __name__ == "__main__":
    test_cases = [
    [3, 6, 1, 0],
    [1, 2, 3, 4],
    [0, 0, 0, 1],
    [1, 0],
    [1, 2],
    [4, 0, 0, 1],
    [5, 0, 10, 0, 1],
    [1, 3, 6, 12, 2, 5],
    [1, 3, 6, 11, 2, 5],
    [100, 1, 50, 49],
    [10, 0, 0, 0, 4],
    [2, 3, 8, 1],
    [7, 1, 0, 3],
    [9, 2, 18, 3, 1],
    [1, 50, 100],
    [10, 5, 4, 3, 1],
    [1, 4, 8, 15, 2, 7],
    [1, 49, 100],
    [2, 4, 8, 16, 3, 7],
    [1, 25, 50, 100]
    ]

    for case in test_cases:
        dominantIndex(case)