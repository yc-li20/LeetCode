class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                i += 1
            elif nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
