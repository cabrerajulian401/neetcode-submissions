class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       # input: nums = [3,4,5,6], target - 7 

       # output: [0,1]

       seen = {}

       for i, num in enumerate(nums): # i is the index & 'and' is the number associated with it
            diff = target - num
            if diff in seen:
                return list((seen[diff],i))

            else:
                seen[num] = i

# seen is a map with a key value pair of {value:index}

        # enumerate function 



