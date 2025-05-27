public class Solution {
    public int MaxArea(int[] height) {
        int l = 0, r = height.Length - 1;
        int area = 0;

        while(l < r) {
            area = Math.Max(area, Math.Min(height[l], height[r]) * (r - l));
            if(height[l] >= height[r]) r--;
            else l++;
        }

        return area;
    }
}