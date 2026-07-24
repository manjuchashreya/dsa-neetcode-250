/*
Problem: Contains Duplicate
Platform: NeetCode 250 / LeetCode
Topic: Arrays & Hashing
Status: Yellow

Approach:
Use an unordered_set to store numbers already seen.
For each number:
- If it already exists in the set, return true
- Otherwise, insert it into the set
If the loop finishes, return false

Important:
seen.count(num) returns:
- 1 if num exists
- 0 if num does not exist

Time Complexity: O(n) average
Space Complexity: O(n)

Mistake:
The logic was correct, but Python-style set syntax was initially used instead of C++ unordered_set syntax.
*/

#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen; // stores unique values

        for (int num : nums) {
            if (seen.count(num)) { // 1 if found, 0 if not found
                return true;
            }

            seen.insert(num);
        }

        return false;
    }
};
