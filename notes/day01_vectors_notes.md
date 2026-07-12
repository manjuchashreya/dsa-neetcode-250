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

| Exercise               | Status      |
| ---------------------- | ----------- |
| Print vector           | Green       |
| Sum vector             | Green       |
| Maximum in vector      | Yellow      |
| Copy vector            | Yellow      |
| Concatenation of Array | Not started |
| Contains Duplicate     | Not started |
