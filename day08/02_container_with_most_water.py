"""
Problem: Container With Most Water
Platform: NeetCode 250 / LeetCode 11
Topic: Two Pointers (opposite direction), greedy move
Date: Oct 31
Status: Green

Goal: pick two lines; the water they hold is min(height[l], height[r]) * width.
Return the max over all pairs. O(n).

Pattern: start l, r at the two ends (widest container). Area is limited by the
SHORTER wall, so move the shorter one inward — the only move that could find a
taller wall and beat the current area. Moving the taller one can never help:
width shrinks and the height is still capped by the shorter wall.

Why greedy is safe: moving the shorter pointer discards only pairs that are
guaranteed <= current area (narrower width, same-or-smaller limiting height),
so no better answer is skipped.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(s.maxArea([1, 1]))                        # 1
    print(s.maxArea([4, 3, 2, 1, 4]))               # 16
    print(s.maxArea([1, 2, 1]))                      # 2
