"""
Problem: Two Sum II - Input Array Is Sorted
Platform: NeetCode 250 / LeetCode 167
Topic: Two Pointers (opposite direction) on a SORTED array
Date: Oct 31
Status: Green

Goal: the array is sorted (1-indexed); return the 1-based indices of the two
numbers that add up to target. Exactly one solution. O(n) time, O(1) space
(better than the hash-map Two Sum because sortedness lets us use two pointers).

Pattern: start l at the smallest and r at the largest.
  sum > target -> the sum is too big  -> move r left  (shrink)
  sum < target -> the sum is too small -> move l right (grow)
  sum == target -> found -> return [l+1, r+1]  (convert to 1-indexed)

Why it can't miss the pair: moving a pointer only discards pairs that are
definitely too big or too small, so the correct pair always stays in range.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []   # problem guarantees a solution, so this is just a fallback


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))    # [1, 2]
    print(s.twoSum([2, 3, 4], 6))         # [1, 3]
    print(s.twoSum([-1, 0], -1))          # [1, 2]
    print(s.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # [4, 5]
