from typing import List

# Kadane's algorithm: O(n) time complexity
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarray = nums[0] # initialize maxSubarray to first element
        currentSum = 0 # initialize currentSum to 0

        for num in nums:
            if currentSum < 0: # if currentSum is negative, reset it to 0; we don't want to add negative numbers from previous subarrays
                currentSum = 0 

            currentSum += num # add current number to currentSum
            maxSubarray = max(maxSubarray, currentSum) # update maxSubarray with the maximum of maxSubarray and currentSum

        return maxSubarray
    
# easy solutions are quadratic and cubic time complexity