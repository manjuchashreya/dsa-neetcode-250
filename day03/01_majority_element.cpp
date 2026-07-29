/*
Problem: Majority Element
Platform: NeetCode 250 / LeetCode
Topic: Arrays & Hashing (Frequency patterns)
Status: Green

Goal: return the element that appears more than n/2 times.
      (The problem guarantees a majority element always exists.)

Four approaches below, from brute force to optimal.
*/

#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

/*
Approach 1: Brute force
For each element, count how many times it appears; return it if count > n/2.

Time:  O(n^2)
Space: O(1)
*/
class SolutionBrute {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (nums[j] == nums[i]) {
                    count++;
                }
            }
            if (count > n / 2) {
                return nums[i];
            }
        }
        return -1;
    }
};

/*
Approach 2: Frequency map
Count occurrences in a hash map; return the value once its count passes n/2.

Time:  O(n)
Space: O(n)
*/
class SolutionMap {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> frequency;
        for (int i = 0; i < n; i++) {
            frequency[nums[i]]++;
            if (frequency[nums[i]] > n / 2) {
                return nums[i];
            }
        }
        return -1;
    }
};

/*
Approach 3: Sorting
After sorting, the majority element must occupy the middle index.

Time:  O(n log n)
Space: O(1)  (ignoring sort's internal space)
*/
class SolutionSort {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }
};

/*
Approach 4: Boyer-Moore Voting Algorithm (optimal)
Idea = cancellation:
- count == 0        -> pick current element as the new candidate
- num == candidate  -> count++
- num != candidate  -> count--
Different values cancel each other; the majority appears more than all
others combined, so it survives as the final candidate.

Note: this returns the candidate directly ONLY because the problem
guarantees a majority exists. Without that guarantee you'd need a second
pass to verify the candidate really is a majority.

Time:  O(n)
Space: O(1)
*/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }

        return candidate;
    }
};
