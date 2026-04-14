class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * (max(nums) - min(nums) + 1)
        res = []

        for num in nums:
            counts[num - min(nums)] += 1
        print(counts)

        index = 0

        for i in range(len(counts)):
            while counts[i] > 0:
                nums[index] = i + min(nums)
                index += 1
                counts[i] -= 1
        return nums


    
        


        
