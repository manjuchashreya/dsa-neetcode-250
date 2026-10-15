"""
Problem: Find Peak Element
Platform: NeetCode 250 / LeetCode 162
Topic: Binary Search on a True/False split (multiple peaks allowed)
Date: Oct 15
Status: Green  (same neighbor logic as 852; needed an out-of-bounds fix)

Goal: nums[i] != nums[i+1]; return the index of ANY peak (nums[i] greater than
both neighbors). nums[-1] and nums[n] count as -infinity. O(log n).

Same climbing/descending logic as 852 — but 852's safety argument does NOT
carry over, which is the lesson: when you reuse code, re-check every array
access for the NEW constraints.
  852: peak is never the last element -> mid never hits last index -> mid+1 safe.
  162: peak CAN be the last element ([1,2,3]) -> the naive copy crashes.

Fix (Option 1, keeps the <= template): shrink h to len-2 so mid never reaches
the last index, making mid+1 always valid. If l climbs all the way to the last
index, that index is the peak (since nums[n] = -inf), and we return l without
ever indexing past the end.
(Option 2 is Template B: h=len-1, while l<h, h=mid, return l.)

Why it works with multiple peaks: if nums[mid] < nums[mid+1], walking right must
eventually hit a peak (it either keeps rising to the end, or turns down); if
nums[mid] > nums[mid+1], the same holds walking left. Each step discards a half
that MIGHT contain a peak but always keeps a half that DEFINITELY does.

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, h = 0, len(nums) - 2      # mid never reaches the last index
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                h = mid - 1
        return l


if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([1, 2, 3, 1]))               # 2
    print(s.findPeakElement([1, 2, 3]))                  # 2 (peak at end, no crash)
    print(s.findPeakElement([1]))                        # 0 (single element)
    print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))      # 5 (any peak; 1 or 5 ok)
    print(s.findPeakElement([3, 2, 1]))                  # 0
