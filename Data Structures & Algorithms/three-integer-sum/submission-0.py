class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ''' 

        input: list[int] -> output : List[list[int]]

        example: [-1,0,1,2,-2,0]

        output: [[-1,0,1],[2,-2,0],[other 0 repetition with |1|],[other 0 rep. with |2|]]

        constraints/possibilites: 

        3 digits need to add up to 0, so use 3 pointers

        After sorting: 
                                    l  
        nums = [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2,2]

        -4 + -1 + 2 = -3 < 0 so we need to move 

        hold that...


        nums[i] + nums[j] + nums[k] == 0 -> nums[i] = -nums[j] - nums[k] 

        - > Key: -nums[i] = nums[j] + nums[k]

    ''' 
        nums.sort()

        results_list = []
        
        for i, j in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            l = i + 1 # have to be distinct
            r = len(nums) - 1 # have to be distinct

            while l < r: 
                
                if nums[l] + nums[r] < target: # 
                    l += 1 

                elif nums[l] + nums[r] > target:
                    r -= 1
                    

                else:

                    results_list.append([nums[l], nums[r],nums[i]])
                    l , r = l + 1, r - 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1 # this line and above one allow you to skip repeated pairs


        return results_list






