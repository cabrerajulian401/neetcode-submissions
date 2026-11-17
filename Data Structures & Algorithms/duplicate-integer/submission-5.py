class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        '''
        inputs: list of ints ; ex: [1,2,4]

        output: bool ex: true, false 
        
        cases: [1,2,3,3] -> true

                [1,2,3,4] -> false
            
             '''


        hash_map = {}

        for i in nums:


            if i in hash_map: 
                return True

            hash_map[i] = i

            

        return False



        


