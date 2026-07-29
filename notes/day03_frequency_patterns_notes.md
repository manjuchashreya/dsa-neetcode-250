# Day 3: Frequency Patterns Notes

## Topic summary

Majority counting, sorting vs hashing trade-offs, the Boyer–Moore Voting
Algorithm, and two-pass frequency problems.

## Problems solved today

| Problem | Pattern | Difficulty | Status | Best Time | Best Space | Code |
| ------- | ------- | ---------- | ------ | --------- | ---------- | ---- |
| Majority Element | Boyer–Moore voting | Easy | Green | O(n) | O(1) | `day03/01_majority_element.cpp` |
| First Unique Character | Frequency count (2-pass) | Easy | Green | O(n) | O(1) | `day03/02_first_unique_character.cpp` |

---

## Majority Element

Condition:

```text
frequency > n / 2
```

Approaches and complexity:

| # | Approach       | Time         | Space |
| - | -------------- | ------------ | ----- |
| 1 | Brute force    | O(n^2)       | O(1)  |
| 2 | Frequency map  | O(n)         | O(n)  |
| 3 | Sorting        | O(n log n)   | O(1)  |
| 4 | Boyer–Moore    | O(n)         | O(1)  |

### Boyer–Moore Voting Algorithm

Rules:

* `count == 0` → choose a new candidate
* same value → `count++`
* different value → `count--`

Why it works:

Different values cancel each other out. The majority element appears more
than all other elements combined, so it can never be fully cancelled — it
survives as the final candidate.

Important caveat:

Boyer–Moore returns a *possible* candidate. It is guaranteed correct here
**only because the problem promises a majority element exists**. Without that
guarantee, add a second pass to verify the candidate actually appears > n/2
times.

```cpp
int candidate = 0, count = 0;
for (int num : nums) {
    if (count == 0) candidate = num;
    if (num == candidate) count++;
    else count--;
}
return candidate;
```

## First Unique Character in a String

Goal: return the index of the first non-repeating character, or `-1` if none.

Why `-1`? Indexes start at `0`, so `-1` means "no valid index exists".

Approaches and complexity:

| # | Approach              | Time   | Space |
| - | --------------------- | ------ | ----- |
| 1 | Brute force           | O(n^2) | O(1)  |
| 2 | Hash map (2-pass)     | O(n)   | O(k)  |
| 3 | Size-26 array (2-pass)| O(n)   | O(1)  |

Map vs array:

* Use a **map** when the character set is broad/unknown or you want a general solution.
* Use a **size-26 array** when input is only lowercase English letters — lower overhead, constant extra space.

For this problem the array is technically preferable, but the map version reinforces the hashing pattern.

### Revision recall

Pattern: character frequency + a second ordered scan.

* **Pass 1:** `frequency[ch]++`
* **Pass 2:** if `frequency[s[i]] == 1`, return `i`

Why two passes?

* Need complete counts first.
* Need the original string order to find the *first* unique character.

Complexity:

* Time: `O(n)`
* Space: `O(k)` with `unordered_map`, `O(1)` with an array of 26

Common mistake: return the **index**, not the character.

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
