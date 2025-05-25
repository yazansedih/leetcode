using System;
using System.Text.RegularExpressions;

public class Solution {
    public bool IsPalindrome(string s) {
         // Convert to lowercase
        s = s.ToLower();
        // Remove non-alphanumeric characters
        s = Regex.Replace(s, "[^a-z0-9]", "");

        int left = 0, right = s.Length - 1;
        while(left < right) {
            if(s[left] != s[right])
                return false;
            left++;
            right--;
        }

        return true;
    }
}