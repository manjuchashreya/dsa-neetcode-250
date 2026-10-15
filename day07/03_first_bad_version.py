"""
Problem: First Bad Version
Platform: NeetCode 250 / LeetCode 278
Topic: Binary Search (boundary — first True), Template A style
Date: Oct 15
Status: Green  (1 fix: return l, not mid)

Versions 1..n look like: good, good, ..., bad, bad. isBadVersion(v) is given.
Find the FIRST bad version with as few calls as possible.

Key: there is NO "found it, return mid" branch. A bad mid might be the first
bad version, or an earlier one might exist — so never return mid. Same loop as
Search Insert (35): when it ends, everything left of l is good and everything
right of h is bad, so l (= h+1) is the first bad version.

Fix made:
  - returned mid (wherever the last check landed = good version) -> return l.
  - l must start at 1 (versions start at 1, not 0).

Style: `if not isBadVersion(mid)` is cleaner than `== False`.

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            mid = (l + h) // 2
            if not isBadVersion(mid):   # noqa: F821  (provided by LeetCode)
                l = mid + 1             # mid is good -> first bad is to the right
            else:
                h = mid - 1             # mid is bad  -> an earlier bad may exist
        return l


if __name__ == "__main__":
    def _make(bad):
        return lambda v: v >= bad

    for n, bad in [(5, 4), (1, 1), (5, 1), (5, 5), (10, 7)]:
        isBadVersion = _make(bad)       # defines module-global `isBadVersion`
        print(f"n={n}, bad={bad} -> {Solution().firstBadVersion(n)}")
