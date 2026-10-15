"""
Problem: Valid Perfect Square
Platform: NeetCode 250 / LeetCode 367
Topic: Binary Search over values (existence check)
Date: Oct 13
Status: Green  (clean, first try, no hints — template is sticking:
                4 bugs on 69 -> 0 bugs here)

Goal: return True if num is a perfect square, else False (no sqrt/pow allowed).
Same loop as Sqrt(x), but we only need whether an exact match EXISTS, so there's
no floor to return — exiting the loop means no integer squares to num -> False.

Time:  O(log n)
Space: O(1)

Interview talking points:
  - l = 1 is valid since num >= 1 (0 can never be the answer); l = 0 just wastes
    one check.
  - Overflow: in C++/Java mid*mid can overflow; use mid < num / mid or long.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, h = 0, num
        while l <= h:
            mid = (l + h) // 2
            if mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                h = mid - 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(16))  # True
    print(s.isPerfectSquare(14))  # False
    print(s.isPerfectSquare(1))   # True
    print(s.isPerfectSquare(2))   # False
    print(s.isPerfectSquare(808201))  # True (899^2)
