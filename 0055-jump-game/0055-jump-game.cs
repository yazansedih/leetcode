public class Solution {
    public bool CanJump(int[] nums) {
        int farthest = 0;
        
        for (int i = 0; i < nums.Length; i++) {
            if (i > farthest) return false; // Can't reach this index
            farthest = Math.Max(farthest, i + nums[i]);
        }

        return true;
    }
}
