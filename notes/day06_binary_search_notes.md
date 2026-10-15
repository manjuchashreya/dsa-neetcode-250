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
| 69 Sqrt(x) | Values + floor return | 🟡 (4 bugs) | O(log x) | O(1) | `day07/01_sqrt.py` |
| 367 Valid Perfect Square | Values, existence check | 🟢 clean | O(log n) | O(1) | `day07/02_valid_perfect_square.py` |
| 278 First Bad Version | Boundary — first True | 🟢 (1 fix) | O(log n) | O(1) | `day07/03_first_bad_version.py` |
| 34 First & Last Position | Duplicates — two boundary searches | 🟢 (key insight) | O(log n) | O(1) | `day07/04_first_last_position.py` |
| 744 Next Greatest Letter | First strictly greater + wrap-around | 🟢 | O(log n) | O(1) | `day07/05_next_greatest_letter.py` |
| 852 Peak in Mountain Array | Neighbor compare (no target) | 🟢 (2 bugs) | O(log n) | O(1) | `day07/06_peak_index_mountain_array.py` |
| 162 Find Peak Element | Neighbor compare, multiple peaks | 🟢 (OOB fix) | O(log n) | O(1) | `day07/07_find_peak_element.py` |

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

## Which pointer holds the answer after the loop? (Template A, no exact match)

After a Template A loop ends with `low > high`, the two pointers straddle the
boundary — and **which one you return depends on the question**:

| Problem | Returns | Meaning |
| ------- | ------- | ------- |
| 35 Search Insert | `low`  | first value that is **>= target** (insert position) |
| 69 Sqrt(x)       | `high` | last value whose square **fits** (floor / rounded down) |
| 367 Perfect Square | — | only need existence → `return False` after the loop |
| 278 First Bad    | `low`  | first **bad** version (first True) |
| 34 first / last  | `low` / `high` | first index `>= target` / last index `<= target` |

Same loop, different question: `low` = "first too big / first True", `high` = "last that fits".

## Duplicates: NEVER return on `==`

When the array has duplicates (34), a match at `mid` only proves the target
**exists** — it might not be the first or last one. So don't return on `==`.
Instead push the `==` case toward the side you're hunting and let `low`/`high`
land on the boundary:

- **First position:** on `==`, go **left** (`high = mid - 1`) → `low` ends on the first index `>= target`.
- **Last position:** on `==`, go **right** (`low = mid + 1`) → `high` ends on the last index `<= target`.

> "equal, go left" feels like throwing away a match, but it's safe: if `mid`
> really was the first one, `low` walks back and lands on it. The invariant
> guarantees the answer is never lost.

This "push equal toward the boundary" idea returns in 744, 852, 162, and the
Level-4 "binary search on the answer" problems.

## Wrap-around with `%` (744)

744 wants the first letter strictly `> target`, wrapping to `letters[0]` if none.
After the loop `l` is in `[0, len]`. Reach for `%` whenever the logic is
**"wrap around / circular"**:

```python
return letters[l % len(letters)]   # l < len -> letters[l];  l == len -> letters[0]
```

It's just a one-line form of `if l == len: return letters[0]; else return letters[l]`.
`%` doesn't create the logic — write the `if` version first (shows you reasoned
the two cases), then compress. Same tool as a clock (`13 % 12 == 1`) or the next
element in a circular array (`nums[(i + 1) % n]`).

## Searching indices vs values

- **704:** search the indices `0 .. len-1` of an array.
- **374:** no array — search the values `1 .. n` directly; an API tells you the
  direction. This is the first step toward **binary search on the answer**.

## Binary search without a sorted array — the True/False split (852, 162)

Binary search doesn't actually need a *sorted* array. It needs a **monotone
True/False split**. Comparing each element with its **neighbor** creates one:

- `arr[mid] < arr[mid+1]` → still **climbing** → a peak is to the right (`l = mid + 1`)
- else → **descending / at peak** → peak is `mid` or left (`h = mid - 1`)

The split is ✅✅❌❌ ("is the next one bigger?"), and the peak is the first ❌ →
return `l` (same as 278 / 744).

**Why it works with multiple peaks (162):** if the right neighbor is bigger,
walking right *must* hit a peak (it keeps rising to the end, or turns down).
Each step discards a half that *might* contain a peak but always keeps a half
that *definitely* does.

**Reuse warning (852 → 162):** the same code, but 852's safety argument does NOT
carry over. In 852 the peak is never the last element, so `mid+1` is always
safe. In 162 the peak *can* be last (`[1,2,3]`), so the naive copy crashes.
Fix: `h = len-2` (Option 1, keeps `<=`) or Template B (`h=len-1`, `while l<h`,
`h=mid`). **Lesson: when you reuse a solution, re-check every array access
against the new constraints.**

## Recurring checklist (run before submitting ANY binary search)

1. Inclusive bounds → `while low <= high` (Template A). *(Write this line FIRST — missed it on 704, 374, and 69.)*
2. **Same variable names everywhere** — don't declare `l, h` then update `low, high` (looks right, does nothing → infinite loop).
3. Comparing `nums[mid]` / `mid*mid`, not `mid` itself?
4. Parentheses: `(low + high) // 2`.
5. Does `low` cover the smallest possible answer (e.g. `0` for Sqrt)?
6. Is there a `return` after the loop?
7. Return value — `low` (just above) or `high` (just below)? Index or value?
8. Every `nums[mid+1]` / `nums[mid-1]`: can `mid` be at an edge? Trace the smallest input (`[1]`, `[1,2]`) before submitting.

> Overflow note: in C++/Java `low + high` can overflow, so use
> `low + (high - low) // 2`. Python ints don't overflow, but mention it.

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
