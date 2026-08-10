// Warm-up: check if a string is a palindrome using two pointers
// Assumes only lowercase letters, no spaces or punctuation.
// "racecar" -> true (1), "hello" -> false (0), "level" -> true (1)
//
// Time:  O(n)
// Space: O(1)

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "racecar";

    int left = 0;
    int right = s.size() - 1;
    bool palindrome = true;

    while (left < right) {
        if (s[left] != s[right]) {
            palindrome = false;
            break;   // early return: no need to check the rest
        }
        left++;
        right--;
    }

    cout << (palindrome ? "true" : "false");

    return 0;
}
