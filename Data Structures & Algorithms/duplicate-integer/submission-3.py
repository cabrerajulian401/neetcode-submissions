class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashMap = {} # Acts as dictionary storing values in a key value pair 
                     # {key: value, key, value }
        
        for i in nums:

            if i not in hashMap: 
                hashMap[i] = i

            else:
                return True 

        return False
