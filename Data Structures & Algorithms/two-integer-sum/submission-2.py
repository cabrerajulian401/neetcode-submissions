class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff = {}

        for i, j in enumerate(nums): # i is index, j is the value
 
            d = target - j

            if d in diff: 
                return [diff[d], i]

            diff[j] = i

        