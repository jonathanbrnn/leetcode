class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        int n = words.size();

        for (int i = 0; i < n; i++)
        {
            int j = 0; 
            int k = words[i].size() - 1;
            bool flag = true; 

            while (j < k)
            {
                if (words[i][j] != words[i][k])
                {
                    flag = false; 
                    j = k; 
                }
                else
                {
                    j++; 
                    k--; 
                }
            } 

            if (flag == true)
            {
                return words[i]; 
            }
        }
        return ""; 
    }
};