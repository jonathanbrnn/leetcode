public class Solution {
    public bool QueryString(string s, int n) {
        for (int i = 1; i < n + 1; i++) {
            if (s.Contains(Convert.ToString(i, 2)) == false)
            {
                return false;
            }
        }
        return true;
    }
}
