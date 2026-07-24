// Frequency count using an unordered_map (key -> value = number -> count)

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    vector<int> nums = {1, 2, 2, 3, 1, 2};

    unordered_map<int, int> frequency;

    for (int num : nums) {
        frequency[num]++;   // creates key if absent, then increments
    }

    for (auto entry : frequency) {
        cout << entry.first << " appears "
             << entry.second << " times\n";
    }

    return 0;
}
