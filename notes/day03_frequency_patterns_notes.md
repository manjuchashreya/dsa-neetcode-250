# Day 3: Frequency Patterns Notes

## Topic summary

Majority counting, sorting vs hashing trade-offs, the Boyer–Moore Voting
Algorithm, and two-pass frequency problems.

## Problems solved today

| Problem | Pattern | Difficulty | Status | Best Time | Best Space | Code |
| ------- | ------- | ---------- | ------ | --------- | ---------- | ---- |
| Majority Element | Boyer–Moore voting | Easy | Green | O(n) | O(1) | `day03/01_majority_element.cpp` |

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

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
