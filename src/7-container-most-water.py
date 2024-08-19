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
    

class Solution2:
    def maxArea(self, height: List[int]) -> int:
        # complexity o(n) solution
        left = 0
        right = len(height) - 1
        max_area = 0
        
        # using the shrinking window with two pointers to find the max area
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            elif height[right] == height[left]:
                right -= 1
            max_area = max(max_area, area)

        return max_area
    
    