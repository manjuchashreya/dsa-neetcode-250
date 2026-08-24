/*
Problem: Intersection of Two Arrays
Platform: NeetCode 250 / LeetCode 349
Topic: Arrays & Hashing (set membership / uniqueness)
Date: Aug 24
Status: Green

Goal: return the UNIQUE values that appear in both arrays (order doesn't matter).

Pattern: hashing for existence. Record the values of nums1, then for each value
in nums2 that is still present, add it to the result and mark it consumed
(set to 0) so it isn't added twice.

Time:  O(n + m)
Space: O(n)

Note: an unordered_set would express "membership" more directly than a map here,
but the map-as-set works fine — zeroing the entry prevents duplicates in output.
*/

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> frequency;
        vector<int> result;
        for (int n : nums1) {
            frequency[n]++;
        }
        for (int n : nums2) {
            if (frequency[n] != 0) {
                result.push_back(n);
                frequency[n] = 0;   // mark consumed -> avoids duplicate output
            }
        }
        return result;
    }
};
