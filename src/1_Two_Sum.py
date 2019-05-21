# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
#   Given nums = [2, 7, 11, 15], target = 9,
#   Because nums[0] + nums[1] = 2 + 7 = 9,
#   return [0, 1].

# Solution 1 - Brute Force
# Time complexity: O(n^2)
# Space complexity: O(1)
def twoSum_bruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]

print(twoSum_bruteForce([2, 7, 11, 15], 9))
