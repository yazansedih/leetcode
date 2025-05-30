public class Solution {
    public int LengthOfLastWord(string s) {
        string[] words = s.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
        return words.Length == 0 ? 0 : words[words.Length - 1].Length;
    }
}
