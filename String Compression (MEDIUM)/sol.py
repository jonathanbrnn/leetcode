from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0

        write_index = 0
        read_index = 0

        while read_index < n:
            char = chars[read_index]
            count = 0
            while read_index < n and chars[read_index] == char:
                read_index += 1
                count += 1

            chars[write_index] = char
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        print(chars)
        return write_index


print(Solution().compress(["a","a","b","b","c","c","c"]))
