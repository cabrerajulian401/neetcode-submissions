class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

       hasMap = {}

       for num in nums:

        if num not in hasMap: 
            hasMap[num] = num 

        else:
            return True

       return False 