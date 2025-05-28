public class Solution {
    public int Jump(int[] nums) {
        int n = nums.Length;
        int jumps = 0;
        int farthest = 0;
        int end = 0;

        for (int i = 0; i < n - 1; i++) {
            farthest = Math.Max(farthest, i + nums[i]);

            // When we reach the end of the current jump,
            // we need to jump and update the range
            if (i == end) {
                jumps++;
                end = farthest;
            }
        }

        return jumps;
    }
}
