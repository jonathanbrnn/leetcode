class Solution {
public:
    int reverse(int x) {
        string _x = to_string(x);

        int sign = 1; 
        int end = 0; 

        if (_x[0] == '-') {
            sign = -1;
            end = 1; 
        }
        else if (_x[0] == '+') {
            end = 1; 
        }

        int i = _x.size() - 1;
        int to_return = 0; 

        while(i > -1 && isdigit(_x[i]))
        {
            int curr_digit = _x[i] - '0'; 

            if (to_return > (INT_MAX - curr_digit) / 10) {
                return 0; 
            }

            to_return = to_return * 10 + curr_digit; 
            i--; 
        } 

        return to_return * sign; 
    }
};
