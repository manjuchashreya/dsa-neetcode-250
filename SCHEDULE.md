# Day-by-Day Schedule (Aug 10 – Aug 20)

Legend: ✅ done · 🟡 in progress · ⬜ not started

---

## ✅ Aug 10 — Day 4: Strings + Two Pointers  🟡 (warm-ups done, 2 problems left)

Concepts: `string`, `char`, `s[i]`, `s.size()`, `isalnum`, `tolower`, opposite-direction two pointers.

Warm-ups:

- [x] Reverse a string (`day04/03_reverse_string.cpp`)
- [x] Simple palindrome check (`day04/04_simple_palindrome.cpp`)

Main problems:

1. [ ] Valid Palindrome
2. [ ] Is Subsequence

Mini-test: explain why two pointers work for palindrome · dry-run `"racecar"`.

## ⬜ Aug 11 — Day 5: Right-to-left + Prefix/Suffix

Concepts: reverse traversal, running maximum, prefix, suffix, prefix/suffix products.

Warm-ups: suffix maximum · prefix sum.

Main problems:

3. [ ] Replace Elements with Greatest Element on Right Side
4. [ ] Product of Array Except Self

Mini-test: build prefix values manually for `[2,3,4]` · explain why Product Except Self can avoid division.

## ⬜ Aug 12 — Day 6: Revision + Hashing Reinforcement

Revision: Contains Duplicate · Valid Anagram · Two Sum · Majority Element.

New related problems:

5. [ ] Ransom Note
6. [ ] Intersection of Two Arrays

Focus: `unordered_map`, `unordered_set`, frequency counting, existence checks.
Timed re-solve: Two Sum or Valid Anagram.

## ⬜ Aug 13 — Day 7: Week 1 Test + Mixed Practice

Revision: one Green problem · two Yellow problems · explain one solution aloud.

New related problems:

7. [ ] Single Number
8. [ ] Move Zeroes

Focus: array traversal, in-place updates, two-pointer intro, XOR intro for Single Number.
Weekly check: identify whether a problem needs Set / Map / Frequency / Two pointers / Prefix-suffix.

## ⬜ Aug 14 — Day 8: Two Pointers in Sorted Arrays

Concepts: sorted-array advantage, left/right pointer movement, why to move left or right, in-place modification.

Warm-ups: pair sum in sorted array · remove duplicates manually.

Main problems:

9. [ ] Two Sum II
10. [ ] Remove Duplicates from Sorted Array

Mini-test: given a sorted array and target, explain which pointer moves and why.

## ⬜ Aug 15 — Day 9: Advanced Two Pointers

Concepts: sort + two pointers, fix-one-element strategy, skipping duplicates, pointer decisions based on sum.

Main problems:

11. [ ] 3Sum
12. [ ] Container With Most Water

Mini-test: explain why 3Sum is `O(n²)` · why brute-force Container With Most Water is `O(n²)`.

## ⬜ Aug 16 — Day 10: Sliding Window Basics

Concepts: what a window is, fixed-size window, variable-size window, expand right, shrink left, window state.

Warm-ups: maximum sum of `k` consecutive elements · sum of every window of size `k`.

Main problems:

13. [ ] Best Time to Buy and Sell Stock
14. [ ] Longest Substring Without Repeating Characters

Mini-test: difference between two pointers and sliding window.

## ⬜ Aug 17 — Day 11: Sliding Window + Frequency

Concepts: window with map/set, removing left-side state, maintaining validity.

Main problems:

15. [ ] Permutation in String
16. [ ] Longest Repeating Character Replacement

Warm-up: count character frequency inside a moving window.
Mini-test: given a window, explain when to shrink it.

## ⬜ Aug 18 — Day 12: Revision + Sliding Window Reinforcement

Revision: Two Sum II · 3Sum · Longest Substring Without Repeating Characters · Best Time to Buy/Sell Stock.

New related problems:

17. [ ] Minimum Size Subarray Sum
18. [ ] Max Consecutive Ones III

Focus: variable sliding window, shrink/expand logic.
Timed re-solve: Longest Substring Without Repeating Characters.

## ⬜ Aug 19 — Day 13: Stack Fundamentals

Concepts: LIFO, `stack<int>`, `push`, `pop`, `top`, `empty`, when a stack is useful.

Warm-ups: push/pop simulation · reverse a sequence with a stack.

Main problems:

19. [ ] Valid Parentheses
20. [ ] Baseball Game

Mini-test: explain why Valid Parentheses is naturally a stack problem.

## ⬜ Aug 20 — Day 14: Stack Patterns + Weekly Test

Concepts: storing previous information, stack of values vs stack of indexes, monotonic stack intro.

Revision: Valid Parentheses · one sliding-window problem · one two-pointer problem.

New related problems:

21. [ ] Min Stack
22. [ ] Daily Temperatures

Weekly test: 1 easy in 20 min · 1 medium in 35–40 min · explain both aloud · state time/space · update tracker.

---

## Coverage target by Aug 20

Core C++/STL: `vector` · `string` · `unordered_set` · `unordered_map` · `stack`

Patterns: array traversal · hashing · frequency counting · number → index · Boyer–Moore ·
prefix/suffix · opposite-direction two pointers · same-direction two pointers ·
sliding window · basic stack · monotonic-stack introduction
