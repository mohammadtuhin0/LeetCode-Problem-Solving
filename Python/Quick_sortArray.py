class Solution:

    def partition(self, nums, l,r):
        key = nums[r]
        start = l

        for i in range(l, r+1):
            if nums[i] <= key:
                temp = nums[i]
                nums[i] = nums[start]
                nums[start] = temp
                start += 1

        return start-1
        
    def quickSort(self, nums, l, r):
        # base case
        if l>=r:
            return 
        p = self.partition(nums, l, r)

        self.quickSort(nums, l, p-1)
        self.quickSort(nums, p+1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.quickSort(nums, 0, n-1)

        return nums