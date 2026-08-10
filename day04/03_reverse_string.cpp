// Warm-up: reverse a string in place using two pointers (opposite direction)
// "interview" -> "weivretni"
//
// Two ways to swap the two characters — both shown below.
//
// Time:  O(n)
// Space: O(1)

#include <iostream>
#include <string>
using namespace std;

// Approach 1: manual swap with a temp variable
string reverseManual(string s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        char temp = s[left];   // use char, not int, for the character type
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
    return s;
}

// Approach 2: std::swap (shorter, preferred in interviews)
string reverseStdSwap(string s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }
    return s;
}

int main() {
    string s = "interview";

    cout << "manual : " << reverseManual(s) << '\n';
    cout << "swap   : " << reverseStdSwap(s) << '\n';

    return 0;
}
