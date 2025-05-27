public class Solution {
    public int DifferenceOfSums(int n, int m) {
        int sum1 = 0;
        int sum2 = 0;
        for (int i = 1; i <= n; i++) {
            if (i % m == 0) sum1 += i;  // divisible by m
            else sum2 += i;             // not divisible by m
        }
        return sum2 - sum1;
    }
}
