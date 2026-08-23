/*
Extra problem (off-plan): 4Sum
Platform: LeetCode 18
Topic: Sorting + Two Pointers
Status: Green

Goal: return all unique quadruplets [a, b, c, d] with a + b + c + d == target.

Pattern family:
  2Sum -> two pointers
  3Sum -> fix 1 element + two pointers
  4Sum -> fix 2 elements + two pointers

Approach progression:
  1. Brute force: 4 nested loops -> O(n^4). Too slow.
  2. Better: fix i, j, then use a hash set for the inner pair -> O(n^3) time, O(n) space.
  3. Optimal: sort, fix i and j, two pointers for the remaining pair,
     skipping duplicates -> O(n^3) time, O(1) extra space (ignoring output).

Note: use long long for the sum to avoid int overflow.
*/

#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

/*
Approach 1 (illustration only) — Brute force, O(n^4):

for (int i = 0; i < n; i++)
  for (int j = i + 1; j < n; j++)
    for (int k = j + 1; k < n; k++)
      for (int l = k + 1; l < n; l++)
        // check if nums[i]+nums[j]+nums[k]+nums[l] == target

Approach 2 (illustration only) — Better, O(n^3) time / O(n) space:

for (int i = 0; i < n; i++)
  for (int j = i + 1; j < n; j++) {
    unordered_set<long long> seen;
    for (int k = j + 1; k < n; k++) {
      long long needed = (long long)target - nums[i] - nums[j] - nums[k];
      if (seen.count(needed)) { ... found quadruplet ... }
      seen.insert(nums[k]);
    }
  }
*/

// Approach 3 — Optimal: sort + fix two + two pointers
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> answer;   // list of quadruplets
        int n = nums.size();

        for (int i = 0; i < n - 3; i++) {           // need 3 more numbers after i
            if (i > 0 && nums[i] == nums[i - 1]) {  // skip duplicate i
                continue;
            }
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {  // skip duplicate j
                    continue;
                }
                int left = j + 1;
                int right = n - 1;
                while (left < right) {
                    long long sum = (long long)nums[i] + nums[j] +
                                    nums[left] + nums[right];

                    if (sum == target) {
                        answer.push_back({nums[i], nums[j], nums[left], nums[right]});
                        left++;
                        right--;
                        while (left < right && nums[left] == nums[left - 1]) {
                            left++;    // skip duplicate left
                        }
                        while (left < right && nums[right] == nums[right + 1]) {
                            right--;   // skip duplicate right
                        }
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return answer;
    }
};
