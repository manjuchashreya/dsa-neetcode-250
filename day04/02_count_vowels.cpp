// Warm-up: count vowels (a, e, i, o, u) in a string
// "education" -> 5
//
// Two ways to test whether a character is a vowel — both shown below.
//
// Time:  O(n)   (the "aeiou" string is only 5 chars, so find() is O(1) per call)
// Space: O(1)

#include <iostream>
#include <string>
using namespace std;

// Approach 1: explicit OR chain
int countVowelsOr(const string& s) {
    int c = 0;
    for (char ch : s) {
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
            c++;
        }
    }
    return c;
}

// Approach 2: look the char up inside "aeiou"
// find() returns string::npos when the character is not present.
int countVowelsFind(const string& s) {
    int c = 0;
    for (char ch : s) {
        if (string("aeiou").find(ch) != string::npos) {
            c++;
        }
    }
    return c;
}

int main() {
    string s = "education";

    cout << "or   : " << countVowelsOr(s) << '\n';
    cout << "find : " << countVowelsFind(s) << '\n';

    return 0;
}
