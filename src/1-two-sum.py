from typing import List 

# simple brute force solution
# complexity: O(n^2)
class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums+1)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]
                

# better solution using hash table
# complexity: O(n)
# 1 - use hash table to store the values and indices
# 2 - iterate through the list and check if the complement of the current value is in the hash table             
class Solution_2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value : index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [i, hashmap[complement]]  