/*
Extra problem (off-plan): Move Zeroes
Platform: LeetCode 283
Topic: Arrays / Two Pointers (same direction)
Status: Green

Goal: move all 0's to the end while keeping the relative order of the
non-zero elements. Must be done in place.

Pattern to remember:
  right scans for useful (non-zero) elements,
  left marks where the next useful element should be placed.

Time:  O(n)
Space: O(1)
*/

#include <vector>
#include <algorithm>
using namespace std;

/*
Approach 1: manual placement (my first version)
When nums[left] is 0, find the next non-zero to its right and move it into
place, zeroing out the source. More bookkeeping than needed, but works.
*/
class SolutionManual {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;
        int right = 1;
        int n = nums.size();
        while (left < n && right < n) {
            if (nums[left] == 0) {
                if (right <= left) {
                    right = left + 1;
                }
                while (right < n && nums[right] == 0) {
                    right++;
                }
                if (right == n) {
                    break;
                }
                nums[left] = nums[right];
                nums[right] = 0;
            }
            left++;
            if (right <= left) {
                right = left + 1;
            }
        }
    }
};

/*
Approach 2: clean swap (preferred)
right scans every element; whenever it finds a non-zero, swap it to the
left pointer and advance left. Zeros naturally bubble to the end.
*/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;
        for (int right = 0; right < nums.size(); right++) {
            if (nums[right] != 0) {
                swap(nums[left], nums[right]);
                left++;
            }
        }
    }
};
