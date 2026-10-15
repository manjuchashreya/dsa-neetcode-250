"""
Problem: Find Smallest Letter Greater Than Target
Platform: LeetCode 744
Topic: Binary Search (boundary — first strictly greater, with wrap-around)
Date: Oct 15
Status: Green  (after fixing: push == to the right, and wrap with %)

Goal: letters is sorted; return the smallest letter STRICTLY greater than
target. Wraps around — if none is greater, return letters[0].

Pattern: this is "first index where letters[i] > target" (a boundary search).
Treat == as "not good enough" and go right, so l lands on the first strictly
greater letter.

  if letters[mid] <= target:  l = mid + 1   # too small OR equal -> go right
  else:                       h = mid - 1   # strictly greater -> maybe answer, look left

After the loop l is the first index > target, in range [0, len]. If l == len
(nothing greater), wrap to 0.

Why `l % len(letters)`:
  - l < len  -> % does nothing -> letters[l]
  - l == len -> % wraps to 0  -> letters[0]  (the required wrap-around)
  It's just a 1-line form of:
      if l == len(letters): return letters[0]
      return letters[l]
  Trigger for reaching for % = "wrap around / circular". (Earlier bug used
  letters[mid+1], which crashes when mid is the last index.)

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l, h = 0, len(letters) - 1
        while l <= h:
            mid = (l + h) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
        return letters[l % len(letters)]


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(['c', 'f', 'j'], 'a'))          # 'c'
    print(s.nextGreatestLetter(['c', 'f', 'j'], 'c'))          # 'f'
    print(s.nextGreatestLetter(['c', 'f', 'j'], 'd'))          # 'f'
    print(s.nextGreatestLetter(['c', 'f', 'j'], 'j'))          # 'c' (wrap)
    print(s.nextGreatestLetter(['c', 'c', 'c', 'f'], 'c'))     # 'f' (dupes)
    print(s.nextGreatestLetter(['x', 'x', 'y', 'y'], 'z'))     # 'x' (wrap)
