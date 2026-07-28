/*
Problem: Two Sum
Platform: NeetCode 250 / LeetCode
Topic: Arrays & Hashing
Status: Green

Goal: return the indices of the two numbers that add up to target.

Approach: One-pass hash map.
For each number, compute what value we still need (target - nums[i]).
If that needed value is already in the map, we found the pair.
Otherwise store the current number with its index and continue.

Time:  O(n)  -- single pass, O(1) average map lookups
Space: O(n)  -- the map can hold up to n entries
*/

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indexMap;   // value -> index
        for (int i = 0; i < nums.size(); i++) {
            int needed = target - nums[i];
            if (indexMap.count(needed)) {
                return {indexMap[needed], i};
            }
            indexMap[nums[i]] = i;
        }
        return {};
    }
};
