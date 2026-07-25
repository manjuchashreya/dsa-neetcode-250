// Finding a target in a vector (linear search)
// Walk through each element; if it matches the target, mark found and stop.
//
// Time Complexity:  O(n) -- worst case scans every element
// Space Complexity: O(1) -- only a bool flag, no extra structure

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    vector<int> nums = {4, 7, 2, 9};
    int target = 7;
    bool found = false;

    for (int num : nums) {
        if (num == target) {
            found = true;
            break;
        }
    }

    if (found) {
        cout << "Found";
    } else {
        cout << "Not found";
    }

    return 0;
}
