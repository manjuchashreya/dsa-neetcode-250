/*
Problem: Remove Duplicates from Sorted Array
Platform: NeetCode 250 / LeetCode 26
Topic: Arrays / Two Pointers (same direction, slow/fast)
Date: Aug 24
Status: Green

Goal: remove duplicates in place so each unique element appears once; return the
new length k. The first k slots of nums must hold the unique values in order.

Pattern: same-direction slow/fast pointers. Since the array is SORTED, duplicates
are adjacent. slow marks the last unique slot; fast scans ahead. When fast finds a
new value, advance slow and copy it in.

Brute force (O(n) time, O(n) space): collect uniques into a separate vector, then
copy back. Optimal below removes the extra space.

Time:  O(n)
Space: O(1)

Common mistake: forgetting the empty-array guard, or returning slow instead of
slow + 1 (slow is an index; the count is index + 1).
*/

#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int slow = 0;
        for (int fast = 1; fast < nums.size(); fast++) {
            if (nums[fast] != nums[slow]) {
                slow++;
                nums[slow] = nums[fast];
            }
        }
        return slow + 1;
    }
};
