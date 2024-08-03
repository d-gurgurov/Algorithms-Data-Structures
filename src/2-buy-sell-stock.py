from typing import List

# complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # buy
        right = 1 # sell
        max_profit = 0

        while right < len(prices):
            # if the price grew and profit is awaited, update the max_profit value
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
            # if a new minimum is found, set left pointer to the position of the right one
                left = right 
            # step with the right pointer
            right += 1

        return max_profit

