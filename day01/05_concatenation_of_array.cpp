/*
Problem: Concatenation of Array
Platform: NeetCode 250 / LeetCode
Topic: Arrays
Status: Green

Approach:
Create an answer vector of size 2 * n.
For each index i:
- Store nums[i] at answer[i]
- Store nums[i] again at answer[n + i]

Time Complexity: O(n)
Space Complexity: O(n), including the returned answer
Mistake: None
*/

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(2 * n);

        for (int i = 0; i < n; i++) {
            answer[i] = nums[i];
            answer[n + i] = nums[i];
        }

        return answer;
    }
};
