class Solution:
    def search(self, nums: List[int], target: int) -> int:

      l = 0

      r = len(nums) - 1

      while l <= r:

        divider = (l+r) // 2 

        if target > nums[divider]:
            l = divider + 1 

        elif target < nums[divider]:
            r = divider - 1 

        else: 
            return divider

      return -1 
