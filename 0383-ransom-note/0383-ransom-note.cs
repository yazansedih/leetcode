public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        // Create an array to count letters (26 lowercase English letters)
        int[] counts = new int[26];

        // Count each character in magazine
        foreach (char c in magazine) {
            counts[c - 'a']++;
        }

        // Check if ransomNote characters can be formed
        foreach (char c in ransomNote) {
            counts[c - 'a']--;
            if (counts[c - 'a'] < 0) {
                return false; // Not enough of character c
            }
        }

        return true;
    }
}
