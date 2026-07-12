#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> nums = {4, 7, 2, 9};

    int maximum = nums[0];
    for (int num : nums) {
        if (num > maximum) {
            maximum = num;
        }
    }

    cout << maximum;
    return 0;
}
