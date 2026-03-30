# Bubble Sort

def sortArray(nums):
        n = len(nums)

        # Bubble Sort
        for i in range(n):
            isSwap = False
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    # swap
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    isSwap = True

            if not isSwap:
                break

        return nums

print(sortArray([3, 2, 4, 6, 7, 1, 8, 11, 15]))