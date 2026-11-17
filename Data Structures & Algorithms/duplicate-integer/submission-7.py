class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        '''
        input: [1,2,4,4] Output: True

        input: [1,2,3,4] Output: True

        Need some way to track the nums that have been iterated over

        seen stores the integers we have seen 

        {1:True, 2:False}

        '''

        seen = {} 

        for i in nums: 

            if i in seen:
                return True

            seen[i] = True # seen[i] means i is the key and rightside expression is the value 

        return False  # if entire loop finishes and if loop does not trigger than the list has no duplicates, outside the for loop after it finishes

        
