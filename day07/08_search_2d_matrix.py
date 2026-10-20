"""
Problem: Search a 2D Matrix
Platform: NeetCode 250 / LeetCode 74
Topic: Binary Search on a grid (flatten m*n into one virtual sorted array)
Date: Oct 20 (revision)
Status: Green

Goal: each row is sorted and the first element of each row > last of the
previous row, so the whole matrix is one sorted sequence read left-to-right,
top-to-bottom. Return True if target is present. O(log(m*n)).

Trick: run a plain 704 binary search over 1D indices 0 .. m*n-1, converting
each index to a grid cell:
    row = mid // cols   # how many FULL rows come before this index
    col = mid %  cols   # how far INTO that row (leftover)
Reverse check: row * cols + col == index.

Why divide by cols (not rows)? A new row starts every `cols` cells, so the
row length decides when the index "wraps" to the next row.

Time:  O(log(m*n))
Space: O(1)
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, h = 0, rows * cols - 1
        while l <= h:
            mid = (l + h) // 2
            val = matrix[mid // cols][mid % cols]
            if val < target:
                l = mid + 1
            elif val > target:
                h = mid - 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(s.searchMatrix(m, 30))   # True
    print(s.searchMatrix(m, 16))   # True
    print(s.searchMatrix(m, 8))    # False (ends l=4, h=3)
    print(s.searchMatrix(m, 1))    # True  (first cell)
    print(s.searchMatrix(m, 60))   # True  (last cell)
    print(s.searchMatrix(m, 61))   # False (past the end)
