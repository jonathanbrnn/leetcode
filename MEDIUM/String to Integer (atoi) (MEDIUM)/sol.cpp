class Solution {
public:
    int myAtoi(string s) {
        int p = 0;
        while (p < s.size() && s[p] == ' ') {
            p++;
        }

        if (p == s.size()) return 0;

        int sign = 1;
        if (s[p] == '-') {
            sign = -1;
            p++;
        } else if (s[p] == '+') {
            p++;
        }

        int to_return = 0;
        while (p < s.size() && isdigit(s[p])) {
            int curr_digit = s[p] - '0';

            if (to_return > (INT_MAX - curr_digit) / 10) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }

            to_return = to_return * 10 + curr_digit;
            p++;
        }

        return to_return * sign;
    }
};
