"""
Problem: Find First and Last Position of Element in Sorted Array
Platform: NeetCode 250 / LeetCode 34
Topic: Binary Search with duplicates (two boundary searches)
Date: Oct 15
Status: Green  (needed the key insight: never return on ==)

Goal: return [first, last] indices of target, or [-1, -1] if absent. O(log n).

THE KEY INSIGHT — with duplicates, never return on a match. A match at mid only
proves target exists; push the == case toward the side you're hunting and let
l / h land on the boundary:
  - First position: on ==, go LEFT  (h = mid - 1) -> l ends on first index >= target
  - Last  position: on ==, go RIGHT (l = mid + 1) -> h ends on last index <= target

Return cheat sheet (Template A, after loop):
  first  -> l  (like 35 / 278: first True)
  last   -> h  (like 69: last that fits)

Why "equal, go left": finding an 8 at mid doesn't prove it's the FIRST 8 — an
earlier 8 may exist. Moving h left checks for one; if mid really was first, l
walks back and lands on it. The answer is never lost (loop invariant).

Time:  O(log n)  (two binary searches)
Space: O(1)
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Search 1: first index with nums[i] >= target  (on ==, go left)
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        first = l

        # Not found: l ran off the end, or landed on a non-target value
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        # Search 2: last index with nums[i] <= target  (on ==, go right)
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
        last = h

        return [first, last]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))   # [3, 4]
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))   # [-1, -1]
    print(s.searchRange([], 0))                     # [-1, -1]
    print(s.searchRange([1], 1))                     # [0, 0]
    print(s.searchRange([8, 8, 8], 8))               # [0, 2]
