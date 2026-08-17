/*
Problem: Is Subsequence
Platform: NeetCode 250 / LeetCode
Topic: Strings / Two Pointers (same direction)
Status: Green

Goal: return true if s is a subsequence of t (all of s's characters appear in
t in the same relative order, not necessarily contiguous).

Approach: Same-direction two pointers.
- i walks through s, j walks through t.
- Whenever s[i] == t[j], that character of s is matched, so advance i.
- Always advance j.
- s is a subsequence exactly when i reaches the end of s (all matched).

Time:  O(n)   where n = t.size()
Space: O(1)
*/

#include <string>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        int j = 0;
        while (i < s.size() && j < t.size()) {
            if (s[i] == t[j]) {
                i++;
            }
            j++;
        }
        return i == s.size();
    }
};
