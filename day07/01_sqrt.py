"""
Problem: Sqrt(x)
Platform: NeetCode 250 / LeetCode 69
Topic: Binary Search over values + floor/boundary return
Date: Oct 13
Status: Yellow  (comparison logic right; 4 bugs — incl. the <= habit again
                 and a new one: mismatched variable names l/h vs low/high)

Goal: return floor(sqrt(x)) = the largest integer k with k*k <= x.
Pattern: ✅✅✅❌❌ is a sorted yes/no, so binary search applies. Search the
VALUES 0..x (like 374), Template A (exact match possible), and when there's no
exact match return the rounded-down pointer.

Key lesson — which pointer after the loop?
  35 Search Insert  -> return low  (first index whose value is >= target)
  69 Sqrt(x)        -> return high (last value whose square still fits = floor)
Same loop, different question.

Bugs caught on first attempt:
  1. l,h = 1,x  -> should be 0,x  (x=0 must work: h=0 < l=1 skips the loop)
  2. while l < h -> should be l <= h   (THIRD repeat; x=1 skipped otherwise)
  3. declared l,h but updated low,high -> names never changed -> infinite loop.
     NEW mistake type: looks right, does nothing. Pick ONE naming style.
  4. no return after the loop -> x=8 (no exact match) returned None. Return h.

Time:  O(log x)
Space: O(1)

Overflow note: in C++/Java mid*mid can overflow; use mid < x / mid, or long.
Python ints don't overflow, but say it in an interview.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l <= h:
            mid = (l + h) // 2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                h = mid - 1
            else:
                return mid
        return h   # no exact match: h holds the floor


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(0))   # 0
    print(s.mySqrt(1))   # 1
    print(s.mySqrt(4))   # 2 (exact)
    print(s.mySqrt(8))   # 2 (floor)
    print(s.mySqrt(16))  # 4
