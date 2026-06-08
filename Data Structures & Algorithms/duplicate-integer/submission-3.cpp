class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size() == 0)
            return false;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i + 1; j < nums.size(); j++){
                if (nums[i] > nums[j]){
                    int a = nums[i];
                    nums[i] = nums[j];
                    nums[j] = a;
                }
            }
        }

        for(int i = 0; i < nums.size() - 1; i++){
            if(nums[i] == nums[i+1]){
                return true;
            }
        }
        return false;
    }
};