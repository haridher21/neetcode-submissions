class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1, cap = 0, max_cap = 0;
        while (l < r){
            cap = min(heights[l], heights[r]) * (r - l);
            if (cap > max_cap) max_cap = cap;
            if (heights[l] < heights[r]) l++;
            else r--;
        }
        return max_cap;
    }
};
