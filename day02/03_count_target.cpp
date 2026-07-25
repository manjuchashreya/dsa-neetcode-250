// Counting how many times a target appears in a vector
// Walk through each element; increment count on every match.
//
// Time Complexity:  O(n) -- must check every element (no early exit)
// Space Complexity: O(1) -- only an int counter, no extra structure

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    vector<int> nums = {1, 2, 2, 3, 2};
    int count = 0;
    int target = 2;

    for (int num : nums) {
        if (num == target) {
            count++;
        }
    }

    cout << count;

    return 0;
}
