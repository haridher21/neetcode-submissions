class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n1, n2;
        for(int i = 0; i < nums.size() - 1; i++){
            for(int j = i + 1; j < nums.size(); j++){
                n1 = nums[i];
                n2 = nums[j];
                if ((n1 + n2) == target)
                    return vector<int>{i, j};
            }
        }
    }
};
