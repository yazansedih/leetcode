public class Solution {
    public int StrStr(string haystack, string needle) {
        if (string.IsNullOrEmpty(needle)) return 0;

        int hLen = haystack.Length;
        int nLen = needle.Length;

        for (int i = 0; i <= hLen - nLen; i++) {
            if (haystack[i] == needle[0]) {
                string s = haystack.Substring(i, nLen);
                if (s == needle) {
                    return i;
                }
            }
        }
        return -1;
    }
}