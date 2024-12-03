class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        if(spaces.empty() || s.empty()) 
        {
            return s; 
        }

        int k = 0; 
        string res = ""; 

        for(int i = 0; i < s.size(); i++) {
            if(k < spaces.size() && i == spaces[k]) 
            {
                res += " ";
                k++;
            }
            res += s[i];
        }

        return res; 
    }
};
