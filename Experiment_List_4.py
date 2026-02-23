# 1/ #Given a sorted array of distinct integers and a target value, return the index if the target
# is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low

# Given an array of distinct integers candidates and a target integer target, return a list of
# all unique combinations of candidates where the chosen numbers sum to target. You
# may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is
# different.
# The test cases are generated such that the number of unique combinations that sum up
# to target is less than 150 combinations for the given input.
