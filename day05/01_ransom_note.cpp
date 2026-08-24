/*
Problem: Ransom Note
Platform: NeetCode 250 / LeetCode 383
Topic: Arrays & Hashing (frequency counting)
Date: Aug 24
Status: Green

Goal: return true if ransomNote can be built from the letters in magazine
(each magazine letter used at most once).

Pattern: frequency counting -> store character -> count of the magazine,
then spend those counts while scanning ransomNote.

Brute force: for each char in ransomNote, linear-search magazine for an unused
copy -> O(n*m). Optimal below uses a hash map.

Time:  O(n + m)   n = ransomNote, m = magazine
Space: O(k)       k = distinct characters (<= 26 for lowercase)

Common mistake: decrementing before checking. Check frequency[ch] == 0 FIRST
(0 means no copy left), otherwise you'd go negative and wrongly allow it.
*/

#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> frequency;
        for (char ch : magazine) {
            frequency[ch]++;
        }
        for (char ch : ransomNote) {
            if (frequency[ch] == 0) {
                return false;
            }
            frequency[ch]--;
        }
        return true;
    }
};
