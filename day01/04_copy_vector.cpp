#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> nums = {1, 2, 3};
    vector<int> copiedNums;

    for (int num : nums) {
        copiedNums.push_back(num);
    }

    for (int num : copiedNums) {
        cout << num << " ";
    }

    return 0;
}
