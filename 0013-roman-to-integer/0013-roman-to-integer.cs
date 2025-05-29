public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> roman = new Dictionary<char, int> {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int total = 0;

        for (int i = 0; i < s.Length; i++) {
            // If the current value is less than the next one, subtract it
            if (i + 1 < s.Length && roman[s[i]] < roman[s[i + 1]]) {
                total -= roman[s[i]];
            } else {
                total += roman[s[i]];
            }
        }

        return total;
    }
}