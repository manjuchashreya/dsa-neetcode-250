"""
Problem: Find Minimum in Rotated Sorted Array
Platform: NeetCode 250 / LeetCode 153
Topic: Binary Search on a rotated array (fixed-landmark comparison)
Date: Oct 21
Status: Yellow  (2 syntax bugs + 1 conceptual bug: compared against a MOVING
                 pointer instead of a fixed landmark)

Goal: a sorted array rotated some amount; return the minimum. O(log n).

Mental model: rotation splits the array into a HIGH piece then a LOW piece:
    [ 4 5 6 7 | 0 1 2 ]   the minimum is the first element of the low piece.
Compare mid against a FIXED landmark nums[-1] (the last element):
    nums[mid] <= nums[-1]  -> mid is in the LOW piece  -> min is mid or left (h = mid - 1)
    else                   -> mid is in the HIGH piece -> min is to the right (l = mid + 1)
When the loop ends, l points at the minimum (same "l walks back to it" safety
net as 34 / 744).

THE KEY LESSON (new, bigger than any Day 1-3 bug):
  In rotated-array problems, always compare against a pointer/landmark that
  stays PUT for the whole search (nums[-1], or nums[h] in 33). NEVER compare
  against the pointer you're actively moving (nums[l]) — its meaning shifts
  mid-search and l can walk straight past the minimum.

Why nums[-1] and not nums[0]? nums[0] can't tell "not rotated at all" from
"high piece" (in both, every element >= nums[0]), so it discards the info you
need. nums[-1] distinguishes the two pieces correctly.

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] <= nums[-1]:
                h = mid - 1      # mid in low piece -> min is mid or left
            else:
                l = mid + 1      # mid in high piece -> min is to the right
        return nums[l]


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))          # 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))    # 0
    print(s.findMin([11, 13, 15, 17]))         # 11 (not rotated)
    print(s.findMin([2, 1]))                    # 1
    print(s.findMin([1]))                        # 1
