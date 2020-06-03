class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
        h=set()
        for i in range(min(len(nums),k+1)):
            if nums[i] in h:

                return True
            else:
                h.add(nums[i])
        for i in range(k+1,len(nums)):
            h.remove(nums[i-k-1])
            if nums[i] in h:
                return True
            else:
                h.add(nums[i])

        return False


