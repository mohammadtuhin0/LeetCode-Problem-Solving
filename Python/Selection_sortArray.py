# Selection Sort

def sortArray(nums):
    n = len(nums)

    for i in range(n):
        mn = nums[i]
        ind = i
        for j in range(i+1, n):
            if nums[j]<mn:
                ind = j
    
        temp = nums[i]
        nums[i] = nums[ind]
        nums[ind] = temp
    
    return nums

print(sortArray([3, 2, 4, 6, 7, 1, 8, 11, 15]))