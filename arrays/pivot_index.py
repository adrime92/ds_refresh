"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the
left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because 
there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. 
If no such index exists, return -1.

e.g.:

[1, 2, 3, 3] --> pivot index would be 2
[3, 5, 1, 7, 2] --> pivot index would be none
"""

def pivot_index(nums):
    index = len(nums)
    arr_sum_left = []
    arr_sum_right = []
    sum_left = 0
    sum_right = 0

    for i in range(index):
        sum_left = 0
        sum_right = 0
        if i == index:
            arr_sum_right.append(0)      
            continue
        for j in range(index):
            if j < i:
                sum_left = sum_left + nums[j]
            if j > i:
                sum_right = sum_right + nums[j]
        arr_sum_left.append(sum_left)
        arr_sum_right.append(sum_right)

    print(arr_sum_left)
    print(arr_sum_right)
    
    pivot = check_for_pivot(arr_sum_left, arr_sum_right)

    print(pivot)
    print()

def check_for_pivot(left, right):
    for i in range(len(left)):
        if left[i] == right[i]:
            return i    
    return -1


if __name__ == "__main__":
    test_cases = [
    [1,7,3,6,5,6],
    [1,2,3,3],
    [3,5,1,7,2],
    [1],
    [0],
    [1,-1,0],
    [],
    [2,1,-1],
    [1,2,3,4,10]
    ]

    for case in test_cases:
        pivot_index(case)