public class Solution {
    public int MaxArea(int[] height) {
        int l = 0, r = height.Length - 1;
        int area = 0;

        while (l < r) {
            int currentArea = Math.Min(height[l], height[r]) * (r - l); 
            area = Math.Max(area, currentArea);

            if (height[l] >= height[r]) r--;
            else l++;
        }

        return area;
    }
}
