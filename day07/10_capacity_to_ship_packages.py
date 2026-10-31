"""
Problem: Capacity To Ship Packages Within D Days
Platform: LeetCode 1011
Topic: Binary Search on the ANSWER (Level 4)
Date: Oct 31
Status: Green

Goal: ship weights (in order) within `days` days; return the minimum ship
capacity that makes it possible.

Big idea — binary search on the answer: there's no array to search. The search
space is the possible CAPACITIES, and a feasibility test can_ship(cap) gives a
monotone ✅ pattern: too-small caps fail, and once a cap works, every larger one
works too (❌❌❌✅✅✅). We binary-search for the first ✅.

Search space bounds:
  low  = max(weights)  -- must at least carry the heaviest single package
  high = sum(weights)  -- one day carries everything

Feasibility (greedy): load the ship until adding the next package would exceed
cap, then start a new day. Feasible if days_used <= days.

Template B (first True): on can_ship(mid) keep mid (h = mid); else l = mid + 1.
Return l = the smallest feasible capacity.

Time:  O(n log(sum - max))   -- each feasibility check is O(n)
Space: O(1)
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            total_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    total_days += 1
                    current_load = 0
                current_load += w
            return total_days <= days

        l = max(weights)
        h = sum(weights)
        while l < h:
            mid = (l + h) // 2
            if can_ship(mid):
                h = mid          # mid works -> maybe smaller also works
            else:
                l = mid + 1      # mid too small -> need bigger
        return l


if __name__ == "__main__":
    s = Solution()
    print(s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # 15
    print(s.shipWithinDays([3, 2, 2, 4, 1, 4], 3))               # 6
    print(s.shipWithinDays([1, 2, 3, 1, 1], 4))                  # 3
