class Solution {
    map<char, int> dic; 
public:
    static bool comp(int a, int b)
    {
        return a >= b; 
    }

    string frequencySort(string s) {
        for (char c : s) {
            dic[c] += 1;
        }

        vector<tuple<int, char>> sortedVec;

        for (map<char, int>::iterator it = dic.begin(); it != dic.end(); it++)
        {
            sortedVec.push_back(tuple<int, char>(it->second, it->first));
        }

        sort(sortedVec.begin(), sortedVec.end());

        string res = "";

        for (int i = sortedVec.size() - 1; i >= 0; i--)
        {
            for (int j = 0; j < get<0>(sortedVec[i]); j++)
            {
                res += get<1>(sortedVec[i]); 
            }
        }

        return res; 
    }
};