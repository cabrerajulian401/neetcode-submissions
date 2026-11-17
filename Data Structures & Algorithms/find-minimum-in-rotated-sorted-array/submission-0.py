class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''

        input - list of ints 

        output - int tthat is minumum 

        constraints: 

        - all elements are unique, so do not to keep track of them 

        pattern : 
            if nums of length n is rotated m times then min is nums[m-n].

        In binary search you need to deteremien the half which contains the minimum. 

        A rotated sorted array has 1 special property:
            1 part is alwasy sorted [3,4,5,6,1,2] (first 4) and the other part contains the rotation and min.

            if the left half is sorted, then the minimum cannot be there, so we search the right half
            if the right half is sorted, then the minimum must be in the left half (or at the midpoint)

            This lets of eliminate half of the array each time and quickly narrow down in Olog(n)
            ''' 

        l, r = 0, len(nums) - 1 

        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:  # this window is sorted, leftmost is its min
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1  # min is in right half
            else:
                r = m - 1
        return res

        



        


