class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashMap = {} 

        for num in nums:
            
            if num not in hashMap:
                hashMap[num] = nums

            else: 
                return True

        return False