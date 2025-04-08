public class Solution {
    public int Reverse(int x) {
        int rev = 0;

        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            // Check for overflow
            if (rev > int.MaxValue / 10 || (rev == int.MaxValue / 10 && digit > 7)) return 0;
            if (rev < int.MinValue / 10 || (rev == int.MinValue / 10 && digit < -8)) return 0;

            rev = rev * 10 + digit;
        }

        return rev;
    }
}
