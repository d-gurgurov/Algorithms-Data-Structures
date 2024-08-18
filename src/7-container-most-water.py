from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force solution
        left = 0
        right = 1
        area = 0

        # using two pointers to iterate over all possible areas
        for i in range(len(height)):
            for j in range(right, len(height)):
                y = min(height[left], height[right])
                x = right - left
                tmp = y * x
                area = max(area, tmp)
                if right == len(height) - 1:
                    break
                right += 1
            left += 1
            if left == len(height) - 1:
                break
            right = left + 1

        return area
    
    