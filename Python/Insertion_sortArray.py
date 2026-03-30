# Insertion Sort 

def sortArray(nums):
    n = len(nums)

    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
    return nums

print(sortArray([3, 2, 4, 6, 7, 1, 8, 11, 15]))