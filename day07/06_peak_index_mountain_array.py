"""
Problem: Peak Index in a Mountain Array
Platform: LeetCode 852
Topic: Binary Search on a True/False split (no target, compare to neighbor)
Date: Oct 15
Status: Green  (2 bugs fixed)

Goal: a strictly increasing-then-decreasing array; return the peak index.

Big idea: binary search does NOT need a sorted array — it needs a True/False
split. Here "is the next element bigger?" gives ✅✅❌❌, and the peak is the
first ❌ (same shape as 278 / 744 -> return l).

  arr[mid] < arr[mid+1]  -> climbing   -> peak is to the right (l = mid + 1)
  else                   -> descending -> peak is mid or left  (h = mid - 1)

Bugs fixed:
  1. h = len(arr)   -> off by one; arr[mid+1] read past the end. Use len(arr)-1.
  2. no return after loop -> return l.

Is mid+1 safe? Yes, with h = len-1: l only advances while climbing, so it never
passes the peak, and a mountain's peak is never the last element -> mid never
reaches the last index. (Good to say aloud in an interview.)

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, h = 0, len(arr) - 1
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1      # climbing -> peak to the right
            else:
                h = mid - 1      # descending/at peak -> peak is mid or left
        return l


if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray([0, 2, 5, 3, 1]))   # 2
    print(s.peakIndexInMountainArray([0, 1, 2, 3, 0]))   # 3
    print(s.peakIndexInMountainArray([0, 10, 5, 2]))     # 1
    print(s.peakIndexInMountainArray([3, 4, 5, 1]))      # 2
