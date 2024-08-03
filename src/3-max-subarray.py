from typing import List

# complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # use set to store unique values

        for num in nums:
            if num in hashset: # if the value is already in the set, return True
                return True
            hashset.add(num)

        return False
