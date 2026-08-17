/*
Problem: Valid Palindrome
Platform: NeetCode 250 / LeetCode
Topic: Strings / Two Pointers
Status: Green

Goal: return true if the string is a palindrome, considering only
alphanumeric characters and ignoring case.

Two approaches below.
*/

#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

/*
Approach 1: Brute force (build cleaned string, compare with its reverse)
Keep only alphanumeric chars, lowercased, then compare to the reversed copy.

Time:  O(n)
Space: O(n)  -- builds the cleaned + reversed strings
*/
class SolutionBrute {
public:
    bool isPalindrome(string s) {
        string cleaned;
        for (char ch : s) {
            if (isalnum(ch)) {
                cleaned.push_back(tolower(ch));
            }
        }
        string reversed = cleaned;
        reverse(reversed.begin(), reversed.end());
        return cleaned == reversed;
    }
};

/*
Approach 2: Optimal (two pointers, in place)
Move left/right inward, skipping non-alphanumeric characters, and compare
lowercased characters. No extra string is built.

Time:  O(n)
Space: O(1)
*/
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;
        while (left < right) {
            while (left < right && !isalnum(s[left])) {
                left++;
            }
            while (left < right && !isalnum(s[right])) {
                right--;
            }
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
