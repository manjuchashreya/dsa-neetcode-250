# Day 6: Binary Search Notes

## Topic summary

Classic binary search and its two templates. Searching over array **indices**
(704), over **values** with an API (374), and returning a **boundary/insert
index** (35). Language: Python.

## Problems solved

| Problem | Pattern | Status | Time | Space | Code |
| ------- | ------- | ------ | ---- | ----- | ---- |
| 704 Binary Search | Template A (exact match) | 🟡 (5 bugs) | O(log n) | O(1) | `day06/01_binary_search.py` |
| 374 Guess Number | Template A over values 1..n | 🟡 (6 bugs) | O(log n) | O(1) | `day06/02_guess_number.py` |
| 35 Search Insert Position | Boundary / insert index | 🟢 clean | O(log n) | O(1) | `day06/03_search_insert_position.py` |

## The core template (A — exact match)

```python
low, high = 0, len(nums) - 1
while low <= high:              # <= : a 1-element window still needs checking
    mid = (low + high) // 2     # parentheses! precedence bug otherwise
    if nums[mid] == target:
        return mid              # return the INDEX, not nums[mid]
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
return -1                        # (or `low` for insert position)
```

## Template A vs Template B

| | Template A (exact) | Template B (boundary) |
| --- | --- | --- |
| Loop | `while low <= high` | `while low < high` |
| Shrink | `high = mid - 1` | `high = mid` (mid might be the answer) |
| `high` init | `len(nums) - 1` | `len(nums)` (answer can be past the end) |
| Use for | "is target here?" | "first index where condition is true" |

**Rule:** `<=` goes with `high = mid - 1`; `<` goes with `high = mid`.
Mixing them causes infinite loops or missed elements.

Search Insert Position written as Template B (find first `nums[i] >= target`):

```python
low, high = 0, len(nums)
while low < high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        high = mid
    else:
        low = mid + 1
return low
```

## Why `low` is the insert position (loop invariant)

At all times: everything left of `low` is `< target`, everything right of
`high` is `> target`. When the loop ends `low == high + 1`, so `low` is the
first index with value `>= target` — exactly where target belongs. Being able
to say this out loud is what separates "memorized" from "understood".

## Searching indices vs values

- **704:** search the indices `0 .. len-1` of an array.
- **374:** no array — search the values `1 .. n` directly; an API tells you the
  direction. This is the first step toward **binary search on the answer**.

## Recurring checklist (run before submitting ANY binary search)

1. Comparing `nums[mid]`, not `mid`?
2. Inclusive bounds → `while low <= high` (Template A).
3. Parentheses: `(low + high) // 2`.
4. Returning what's asked — index or value?
5. Search space — indices (`0..len-1`) or values (`1..n`)?

> Overflow note: in C++/Java `low + high` can overflow, so use
> `low + (high - low) // 2`. Python ints don't overflow, but mention it.

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
