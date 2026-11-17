class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''

        Use two pointers to calculate the profit using the following key: 

        - right pointer is the day you are selling 

        - left pointer is the day your are buying

        so profit = r - l 

        input: List[int] output: int 

        example: [10,1,5,6,7,1] output : 6 with 7 - 1 = 6 

        '''

        

        l = 0 

        max_profit = 0

        for right in range(len(prices)):
            print(right)

            if prices[right] < prices[l]:
                l = right
                
            print(prices[right])
            curr_profit = prices[right] - prices[l]

            if curr_profit > max_profit:
                max_profit = curr_profit


        return max_profit 



