public class Solution {
    public void Rotate(int[] nums, int k) {
        int n = nums.Length;
        k = k % n; // Handle cases where k > n
        
        Reverse(nums, 0, n - 1);   // Step 1: Reverse the entire array
        Reverse(nums, 0, k - 1);   // Step 2: Reverse first k elements
        Reverse(nums, k, n - 1);   // Step 3: Reverse the rest
    }

    private void Reverse(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}
