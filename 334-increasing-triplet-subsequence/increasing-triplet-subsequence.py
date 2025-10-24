class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1=max(nums)
        min2=float('inf')
        min3=float('inf')
        for i in nums:
            if i<=min1:
                min1=i
            elif i<=min2:
                min2=i
            else:
                return True
        return False 

        
                 

                
        