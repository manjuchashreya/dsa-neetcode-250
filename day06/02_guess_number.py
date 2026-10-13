"""
Problem: Guess Number Higher or Lower
Platform: NeetCode 250 / LeetCode 374
Topic: Binary Search (searching over VALUES, not indices)
Date: Oct 12
Status: Yellow  (API semantics read correctly; 6 bugs on first attempt,
                 two of them repeats from 704: `l < h` and returning wrong thing)

guess(num) API (provided by LeetCode):
  -1 if num is higher than the picked number  (guess too high -> go left)
   1 if num is lower  than the picked number  (guess too low  -> go right)
   0 if num == picked

Pattern: same binary-search template as 704, but there's no array. The search
space is the numbers 1..n directly, and guess(mid) replaces nums[mid] vs target.
This is the first step toward "binary search on the answer".

Time:  O(log n)
Space: O(1)

Bugs caught on first attempt:
  1. redefined/empty guess() -> delete it, LeetCode provides it
  2. l,h = 0,n-1 -> should be 1,n (searching values 1..n, not indices)
  3. while l < h -> should be l <= h   (REPEAT from 704)
  4. mid never assigned -> compute mid inside the loop
  5. guess(mid) called twice -> store res = guess(mid) (API calls can be costly)
  6. return n[mid] -> n is an int; return mid   (REPEAT: return the right thing)
"""


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)          # noqa: F821  (provided by LeetCode)
            if res == 0:
                return mid
            elif res == -1:           # guess too high -> search left
                high = mid - 1
            else:                     # res == 1, guess too low -> search right
                low = mid + 1
        return -1


if __name__ == "__main__":
    # Local test stub for guess(). On LeetCode this is provided for you.
    def _make_guess(pick):
        def guess(num):
            if num > pick:
                return -1
            if num < pick:
                return 1
            return 0
        return guess

    for n, pick in [(10, 6), (1, 1), (10, 1), (10, 10)]:
        guess = _make_guess(pick)        # defines module-global `guess`
        print(f"n={n}, pick={pick} -> {Solution().guessNumber(n)}")
