using System;
using System.Collections.Generic;

public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();
        Dictionary<char, char> brackets = new Dictionary<char, char> {
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };

        foreach (char c in s) {
            if (brackets.ContainsValue(c)) {
                stack.Push(c); 
            } else if (brackets.ContainsKey(c)) {
                if (stack.Count == 0 || stack.Pop() != brackets[c]) {
                    return false; 
                }
            }
        }

        return stack.Count == 0;
    }
}
