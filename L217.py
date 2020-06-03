class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict=set()
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict.add(nums[i])
        return False