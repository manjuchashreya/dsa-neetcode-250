# Day 4: Strings and Two Pointers Notes

## Topic summary

C++ strings in depth, character functions from `<cctype>`, and the two-pointer
technique (opposite-direction and same-direction). Leads into Valid Palindrome
and Is Subsequence.

## Strings basics

A string is a sequence of characters with zero-based indexing (like vectors).

```cpp
string word = "hello";
//  char: h e l l o
//  index:0 1 2 3 4
cout << word[0]; // h
```

Last valid index = `word.size() - 1`.

### Creating strings

```cpp
string s;             // empty -> ""
string s = "hello";   // with value
char ch = 'a';        // 'a' = char  (single quotes)
string s = "a";       // "a" = string (double quotes)
```

### Size / length

`s.size()` and `s.length()` mean the same thing. Use `s.size()` for DSA consistency.

### Looping

```cpp
for (char ch : s) { ... }              // when you only need characters
for (int i = 0; i < s.size(); i++) {}  // when you need the index
```

### Strings are mutable

```cpp
string s = "hello";
s[0] = 'H';   // -> "Hello"
```

## Important string operations

```cpp
s.push_back('o');   // add a char (NOT s.push_back("o") -- that's wrong)
s.pop_back();       // remove last char
string r = a + b;           // concatenate
string r = a + " " + b;     // with a space
a == b;  a != b;            // compare directly
```

## Character functions — `#include <cctype>`

| Function      | Checks / does                | Example                     |
| ------------- | ---------------------------- | --------------------------- |
| `isalpha(c)`  | is a letter                  | `isalpha('7')` -> false     |
| `isdigit(c)`  | is a digit                   | `isdigit('8')` -> true      |
| `isalnum(c)`  | is a letter OR digit         | `isalnum(',')` -> false     |
| `tolower(c)`  | uppercase -> lowercase       | `tolower('A')` -> 'a'       |
| `toupper(c)`  | lowercase -> uppercase       | `toupper('a')` -> 'A'       |

## Two pointers

Using two indexes to inspect different positions.

### Opposite directions (for palindrome, Two Sum II, Container With Most Water, reversing)

```cpp
int left = 0, right = s.size() - 1;
while (left < right) {
    if (s[left] != s[right]) return false;
    left++;
    right--;
}
return true;   // Time O(n), Space O(1)
```

`r a c e c a r` → L and R move inward until `left >= right`. On a mismatch (e.g.
`"hello"`), return `false` immediately — an **early return**.

### Same direction (slow/fast — for removing duplicates, moving zeroes, cycle
detection, subsequence problems)

```
slow →
fast   →
```

Day 4 uses both: Valid Palindrome (opposite), Is Subsequence (same direction).

## Warm-up solutions

Saved in `day04/`:

1. `01_print_characters.cpp` — print each character
2. `02_count_vowels.cpp` — count a/e/i/o/u ("education" -> 5)
3. `03_reverse_string.cpp` — reverse via two pointers ("hello" -> "olleh")
4. `04_simple_palindrome.cpp` — two-pointer palindrome check ("racecar" -> true)

## Key reminders

* `1 = true`, `0 = false` when printing a bool.
* Opposite pointers move `left++; right--;`.
* Use `while (left < right)` — once pointers meet/cross, all pairs are compared.
* `push_back` takes a **char** `'x'`, not a string `"x"`.

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
