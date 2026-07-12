#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> nums(4, 5);

    int sum = 0;
    for (int num : nums) {
        sum += num;
    }

    cout << sum;
    return 0;
}
