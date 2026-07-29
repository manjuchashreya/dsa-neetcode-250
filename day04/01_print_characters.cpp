// Warm-up: print every character of a string on its own line

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "hello";

    for (char ch : s) {
        cout << ch << '\n';
    }

    return 0;
}
