"""
Problem: Search Insert Position
Platform: NeetCode 250 / LeetCode 35
Topic: Binary Search (boundary / insert index)
Date: Oct 12
Status: Green  (clean, first try)

Goal: return the index of target in a sorted array, or the index where it
would be inserted to keep the array sorted.

Why return `low`? Loop invariant: at all times everything left of `low` is
< target and everything right of `high` is > target. When the loop ends
low == high + 1, so `low` is the first index whose value is >= target --
exactly where target belongs.

Time:  O(log n)
Space: O(1)

Template note:
  Template A (exact match, high = mid - 1): use while low <= high  <- this file
  Template B (boundary,   high = mid):      use while low <  high
  Don't mix them (causes infinite loops / missed elements).
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))   # 2  (found)
    print(s.searchInsert([1, 3, 5, 6], 2))   # 1  (insert)
    print(s.searchInsert([1, 3, 5, 6], 7))   # 4  (past the end)
    print(s.searchInsert([1, 3, 5, 6], 0))   # 0  (before all)
    print(s.searchInsert([1], 2))            # 1
