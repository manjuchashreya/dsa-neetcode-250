/*
Problem: First Unique Character in a String
Platform: NeetCode 250 / LeetCode
Topic: Arrays & Hashing (Frequency patterns)
Status: Green

Goal: return the index of the first non-repeating character, or -1 if none.

Why return -1?
Indexes start at 0, so -1 is used to mean "no valid index exists".

Three approaches below, from brute force to optimal.
*/

#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

/*
Approach 1: Brute force
For each character, count its occurrences across the whole string.
The first one with count == 1 is the answer.

Time:  O(n^2)
Space: O(1)
*/
class SolutionBrute {
public:
    int firstUniqChar(string s) {
        for (int i = 0; i < s.size(); i++) {
            int count = 0;
            for (int j = 0; j < s.size(); j++) {
                if (s[i] == s[j]) {
                    count++;
                }
            }
            if (count == 1) {
                return i;
            }
        }
        return -1;
    }
};

/*
Approach 2: Hash map (two pass)
Pass 1: count every character. Pass 2: return the first index whose count is 1.

Time:  O(n)
Space: O(k)  where k = number of distinct characters
*/
class SolutionMap {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> frequency;
        for (char ch : s) {
            frequency[ch]++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (frequency[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};

/*
Approach 3: Size-26 array (lowercase English letters, optimal)
Same two-pass idea, but a fixed 26-slot array indexed by (ch - 'a').

Time:  O(n)
Space: O(1)  -- the array is always 26 slots, independent of input size

Map vs array:
- Use a map when the character set is broad/unknown or you want a general
  solution.
- Use a size-26 array when input is only lowercase English letters and you
  want lower overhead / constant extra space.
For this problem the array is technically preferable, but the map version
reinforces the hashing pattern.
*/
class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> frequency(26, 0);

        for (char ch : s) {
            frequency[ch - 'a']++;
        }

        for (int i = 0; i < s.size(); i++) {
            if (frequency[s[i] - 'a'] == 1) {
                return i;
            }
        }

        return -1;
    }
};
