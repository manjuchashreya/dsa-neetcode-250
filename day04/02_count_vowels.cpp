// Warm-up: count vowels (a, e, i, o, u) in a string
// "education" -> 5
//
// Time:  O(n)
// Space: O(1)

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "education";
    int count = 0;

    for (char ch : s) {
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            count++;
        }
    }

    cout << count;

    return 0;
}
