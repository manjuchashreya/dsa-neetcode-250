/*
Problem: Valid Anagram
Platform: NeetCode 250 / LeetCode
Topic: Arrays & Hashing
Status: Green

Goal: return true if t is an anagram of s (same characters, same counts).

Three approaches below, from brute force to optimal.
*/

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

/*
Approach 1: Brute force (sorting)
Sort both strings; anagrams become identical.

Time:  O(n log n)  -- dominated by sorting
Space: O(1) to O(n) -- depends on the sort implementation
*/
class SolutionSort {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return (s == t);
    }
};

/*
Approach 2: Optimal (hash map counting)
Count each char in s, then subtract using t. If any count goes negative,
t has a character s doesn't have enough of -> not an anagram.

Time:  O(n)
Space: O(k) where k = number of distinct characters (<= 26 for lowercase,
       but general for any charset like Unicode)
*/
class SolutionMap {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> frequency;
        if (s.size() != t.size()) {
            return false;
        }
        for (char ch : s) {
            frequency[ch]++;
        }
        for (char ch : t) {
            frequency[ch]--;
            if (frequency[ch] < 0) {
                return false;
            }
        }
        return true;
    }
};

/*
Approach 3: Better for lowercase English letters only
Use a fixed size-26 array indexed by (ch - 'a') instead of a hash map.
Same idea as approach 2 but with less overhead.

Time:  O(n)
Space: O(1) -- the array is always 26 slots, independent of input size
*/
class SolutionArray {
public:
    bool isAnagram(string s, string t) {
        vector<int> frequency(26, 0);
        if (s.size() != t.size()) {
            return false;
        }
        for (char ch : s) {
            frequency[ch - 'a']++;
        }
        for (char ch : t) {
            frequency[ch - 'a']--;
            if (frequency[ch - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};
