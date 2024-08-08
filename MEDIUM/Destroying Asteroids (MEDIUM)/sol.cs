using System;

public class Solution {
    public bool AsteroidsDestroyed(int mass, int[] asteroids) {
        Array.Sort(asteroids);
        int n = asteroids.Length;
        for (int i = 0; i < n; i++)
        {
            if(asteroids[n - 1] < mass)
            {
                return true;
            }
            else if (asteroids[i] <= mass)
            {
                mass += asteroids[i];
            }
            else
            {
                return false;
            }
        }
        return true;
    }
}
