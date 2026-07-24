# Day 2: Arrays and Hashing Basics Notes

## Topic summary

`unordered_map` stores data as **key → value** pairs, backed by a hash table.
Use it whenever you need to associate extra information with a value (a count, an
index, etc.) or look something up quickly. Average time for insert, search, and
update is `O(1)`.

## Key syntax / concepts

```cpp
#include <unordered_map>
using namespace std;

unordered_map<int, int> mp;   // key type, value type
```

### a. Insert values

```cpp
mp[10] = 5;   // 10 -> 5
```

### b. Access the value

```cpp
cout << mp[10];   // prints 5
```

### c. Update the value

```cpp
mp[10] = 7;   // 10 -> 7
```

### d. Frequency counting

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    vector<int> nums = {1, 2, 2, 3, 1, 2};
    unordered_map<int, int> frequency;

    for (int num : nums) {
        frequency[num]++;   // creates key if not present, then adds 1
    }

    cout << frequency[1] << '\n';   // 2
    cout << frequency[2] << '\n';   // 3
    cout << frequency[3] << '\n';   // 1
    return 0;
}
```

### e. Checking whether a key exists

```cpp
mp.count(key);   // 0 = not present, 1 = present
```

- `count()` only checks whether the key exists — it does **not** modify the map.
- `mp[key]` **inserts** the key (with a default value of 0) if it isn't already there. Be careful using `mp[key]` just to "check" — it silently creates entries.

### f. Looping through an unordered_map

```cpp
for (auto entry : frequency) {
    cout << entry.first << " " << entry.second << '\n';
}
```

- `entry.first` = key, `entry.second` = value.
- The order is **not** maintained — it may differ from insertion order.

### g. Character frequency

You can count characters too, using `char` as the key type:

```cpp
string s = "banana";
unordered_map<char, int> frequency;

for (char ch : s) {
    frequency[ch]++;
}
```

### h. Store value and index

```cpp
indexMap[nums[i]] = i;   // maps a value to the index where it appears
```

## unordered_map vs unordered_set

| Structure       | Stores            | Use when                                    |
| --------------- | ----------------- | ------------------------------------------- |
| `unordered_map` | key → value pairs | you need extra info attached to each value  |
| `unordered_set` | values only       | you only need to know if a value exists     |

## Complexity

Average complexity for insert, search, and update = `O(1)`.

## Revision schedule

- [ ] Review after 1 day
- [ ] Review after 3 days
- [ ] Review after 7 days
- [ ] Review after 14 days
