# Day 1: Vector Revision Notes

## Creating vectors

```cpp
vector<int> nums;
```

Creates an empty integer vector.

```cpp
vector<int> nums = {1, 2, 3};
```

Creates a vector containing 1, 2, and 3.

```cpp
vector<int> nums(4, 5);
```

Creates four elements, each with the value 5:

```text
[5, 5, 5, 5]
```

## Important vector operations

```cpp
nums[i]
```

Access the element at index `i`.

```cpp
nums.size()
```

Return the number of elements.

```cpp
nums.push_back(value);
```

Add a value to the end.

```cpp
nums.pop_back();
```

Remove the last element.

## Loop through a vector

```cpp
for (int num : nums) {
    cout << num << " ";
}
```

## Important mistakes

1. Use `<vector>`, not `<vector.h>`.
2. Use `<iostream>` for `cout` and `cin`.
3. Every C++ statement normally ends with a semicolon.
4. This:

```cpp
vector<int> nums(4, 5);
```

does not create `[4, 5]`. It creates `[5, 5, 5, 5]`.

5. When finding the maximum, do not always start with zero:

```cpp
int maximum = nums[0];
```

This also works when every number is negative.

6. Call `push_back()` on the destination vector:

```cpp
copiedNums.push_back(num);
```

7. A correct index loop uses:

```cpp
for (int i = 0; i < nums.size(); i++)
```

Do not use:

```cpp
i <= nums.size()
```

because the last valid index is `nums.size() - 1`.

## Current status

| Exercise               | Status      | Time       | Space |
| ---------------------- | ----------- | ---------- | ----- |
| Print vector           | Green       | O(n)       | O(1)  |
| Sum vector             | Green       | O(n)       | O(1)  |
| Maximum in vector      | Yellow      | O(n)       | O(1)  |
| Copy vector            | Yellow      | O(n)       | O(n)  |
| Concatenation of Array | Green       | O(n)       | O(n)  |
| Contains Duplicate     | Yellow      | O(n) avg   | O(n)  |

Space notes:

* **Print / Sum / Maximum** — O(1) *auxiliary* space: only a single variable is used, no new container. The input itself is not counted.
* **Copy / Concatenation / Contains Duplicate** — O(n) because a new structure grows with the input.
* **Concatenation result vector** — the `answer` vector has size `2 * n`. Constant factors are dropped, so `2n` is still **O(n)**. Also, by convention the *returned* array is often called the "output" and not counted as extra space — but the honest total (output included) is still O(n), so it doesn't change the answer here.

## Concatenation of Array

Given:

```text
nums = [1, 2, 1]
```

Return:

```text
[1, 2, 1, 1, 2, 1]
```

Important idea:

```cpp
int n = nums.size();
vector<int> answer(2 * n);

for (int i = 0; i < n; i++) {
    answer[i] = nums[i];
    answer[n + i] = nums[i];
}
```

The second copy begins at index `n`.
Example when `n = 3`:

```text
First copy indexes:  0, 1, 2
Second copy indexes: 3, 4, 5
```

Complexity:

* Time: `O(n)`
* Space: `O(n)`

Status: Green

## Contains Duplicate

Goal:

Return `true` if any number appears more than once.

Example:

```text
nums = [1, 2, 3, 1]
answer = true
```

Important C++ syntax:

```cpp
unordered_set<int> seen;
```

Check whether a number already exists:

```cpp
if (seen.count(num)) {
    return true;
}
```

Insert a number:

```cpp
seen.insert(num);
```

Meaning of `count()`:

* `0` means not found
* `1` means found

Complete pattern:

```cpp
unordered_set<int> seen;

for (int num : nums) {
    if (seen.count(num)) {
        return true;
    }

    seen.insert(num);
}

return false;
```

Complexity:

* Time: `O(n)` average
* Space: `O(n)`

Status: Yellow
Reason: The approach was understood, but C++ `unordered_set` syntax required help.
