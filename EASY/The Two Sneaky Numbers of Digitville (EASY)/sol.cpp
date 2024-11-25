class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        vector<int> res;
        int l = nums.size();
         

        for(int i = 0; i < l; i++)
        {
            for(int j = 1; j < l - i; j++)
            {
                if(nums[i] == nums[j + i])
                {
                    res.push_back(nums[i]);
                }
            }
        }
        return res; 
    }
};