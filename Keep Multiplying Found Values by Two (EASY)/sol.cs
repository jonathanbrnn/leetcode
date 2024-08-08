public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        while (true) {
            bool found = false;
            for(int i = 0; i < nums.Length; i++)
            {
                if (nums[i] == original)
                {
                    original *= 2;
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                return original;
            }
        }
    }
}
