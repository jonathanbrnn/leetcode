class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        vector<int> row(grid.size(), 0); 
        vector<int> col(grid[0].size(), 0);

        for(int i = 0; i < grid.size(); i++)
        {
            for(int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j] == 1)
                {
                    row[i]++; 
                    col[j]++;
                }
                else
                {
                    row[i]--; 
                    col[j]--; 
                }
            }
        }

        for(int i = 0; i < grid.size(); i++)
        {
            for(int j = 0; j < grid[0].size(); j++)
            {
                grid[i][j] = row[i] + col[j];
            }
            
        }
        
        return grid; 
    }
};