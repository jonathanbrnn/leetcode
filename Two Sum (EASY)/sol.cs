using System;
using System.Collections.Generic;

class Solution
{
    private List<int> input = new List<int> { 2, 4, 10, 11, 3, 8 };
    private int target = 9;

    static void Main(string[] args)
    {
        Solution solution = new Solution();
        solution.FindPairs();
    }

    public void FindPairs()
    {
        input.Sort();
        int left = 0;
        int right = input.Count - 1;
        while (left < right)
        {
            int current = input[left] + input[right];
            if (current == target)
            {
                Console.WriteLine(input[left] + ", " + input[right]);
                return;
            }
            else if (current < target)
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        Console.WriteLine("None found");
    }
}