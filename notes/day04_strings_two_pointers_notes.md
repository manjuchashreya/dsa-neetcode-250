# Day 4: Strings and Two Pointers Notes

## Topic summary

C++ strings in depth, the important character functions from `<cctype>`, and the
two-pointer technique (opposite-direction and same-direction). Leads into Valid
Palindrome and Is Subsequence.

## Work done today

| Item | Type | Status | Code |
| ---- | ---- | ------ | ---- |
| Print characters   | Warm-up | Green | `day04/01_print_characters.cpp` |
| Count vowels       | Warm-up | Green | `day04/02_count_vowels.cpp` |
| Reverse a string   | Warm-up | Green | `day04/03_reverse_string.cpp` |
| Simple palindrome  | Warm-up | Green | `day04/04_simple_palindrome.cpp` |
| Valid Palindrome   | Main    | Green | `day04/05_valid_palindrome.cpp` |
| Is Subsequence     | Main    | Green | `day04/06_is_subsequence.cpp` |

---

## Part 1 — String basics

A string is a sequence of characters, with zero-based indexing (like vectors).

```cpp
string s = "hello";
//  char:  h e l l o
//  index: 0 1 2 3 4

s[0]      // 'h'
s[1]      // 'e'
s.size()  // 5
```

The last valid index is `s.size() - 1`.

`char` vs `string`:

```cpp
char ch = 'a';   // 'a' = one character  (single quotes)
string s = "a";  // "a" = string         (double quotes)
```

## Part 2 — Looping through strings

When you need only the characters:

```cpp
for (char ch : s) {
    cout << ch << " ";
}
```

When you need the indexes:

```cpp
for (int i = 0; i < s.size(); i++) {
    cout << s[i] << " ";
}
```

Interview rule: **need the index? use an index-based loop.**

## Part 3 — Useful character functions

Include `<cctype>` (already available with `bits/stdc++.h`).

| Function     | Checks / does           | Examples                                   |
| ------------ | ----------------------- | ------------------------------------------ |
| `isalnum(c)` | letter OR digit         | `isalnum('A')`,`isalnum('7')` → true; `isalnum(' ')`,`isalnum(',')` → false |
| `tolower(c)` | uppercase → lowercase   | `tolower('A')` → 'a'; `tolower('G')` → 'g' |
| `isalpha(c)` | is a letter             | `isalpha('A')` → true; `isalpha('5')` → false |
| `isdigit(c)` | is a digit              | `isdigit('8')` → true; `isdigit('x')` → false |

For **Valid Palindrome**, the two important ones are `isalnum()` and `tolower()`.

## Part 4 — String operations

```cpp
s.push_back('o');   // add a char (NOT s.push_back("o") -- that's wrong)
s.pop_back();       // remove last char
string r = a + b;           // concatenate
string r = a + " " + b;     // with a space
a == b;  a != b;            // compare directly
```

Strings are **mutable**: `s[0] = 'H';` changes `"hello"` → `"Hello"`.

## Part 5 — Two pointers

Using two indexes to inspect different positions.

### Opposite directions

Used for: palindrome, Two Sum II, Container With Most Water, reversing.

```cpp
int left = 0, right = s.size() - 1;
while (left < right) {
    if (s[left] != s[right]) return false;   // mismatch -> early return
    left++;
    right--;
}
return true;   // Time O(n), Space O(1)
```

`r a c e c a r` → L and R move inward until `left >= right`.

### Same directions (slow / fast)

Used for: removing duplicates, moving zeroes, cycle detection, subsequence problems.

```
slow →
fast   →
```

Day 4 uses both — Valid Palindrome (opposite), Is Subsequence (same direction).

## Common mistakes

1. `push_back` takes a **char** `'x'`, not a string `"x"`.
2. When printing a bool: `1 = true`, `0 = false`.
3. Use `while (left < right)` — once pointers meet/cross, all pairs are compared.

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
