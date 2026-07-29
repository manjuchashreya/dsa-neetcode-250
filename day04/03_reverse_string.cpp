// Warm-up: reverse a string in place using two pointers (opposite direction)
// "hello" -> "olleh"
//
// Time:  O(n)
// Space: O(1)

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "hello";

    int left = 0;
    int right = s.size() - 1;

    while (left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }

    cout << s;

    return 0;
}
