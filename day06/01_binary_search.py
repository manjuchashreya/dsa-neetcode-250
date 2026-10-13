"""
Problem: Binary Search
Platform: NeetCode 250 / LeetCode 704
Topic: Binary Search
Date: Oct 12
Status: Yellow  (algorithm structure was right; 5 common binary-search bugs
                 needed correcting on the first attempt)

Goal: given a sorted array of distinct ints and a target, return the target's
index, or -1 if absent. Must run in O(log n).

Pattern: keep an inclusive window [low, high] that could still contain the
target. Check the middle; because the array is sorted, one comparison tells
you which half to discard.

Time:  O(log n)  -- the window halves each iteration
Space: O(1)

The 5 bugs caught on the first attempt (worth memorizing):
  1. Used .size() instead of len(nums)           (that's C++/Java, not Python)
  2. while low < high  -> should be low <= high   (a 1-element window still needs checking)
  3. mid = low + high // 2 -> precedence bug       (write (low + high) // 2)
  4. compared mid to target -> compare nums[mid]   (mid is an index, nums[mid] is the value)
  5. returned nums[mid] -> should return mid        (problem asks for the INDEX)

Takeaway checklist for every binary search:
  - Comparing nums[mid], not mid?
  - Inclusive bounds -> while low <= high
  - Parentheses: (low + high) // 2
  - Returning what's asked: index or value?
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(s.search([-1, 0, 3, 5, 9, 12], 2))   # -1
    print(s.search([5], 5))                      # 0
    print(s.search([5], 3))                      # -1
