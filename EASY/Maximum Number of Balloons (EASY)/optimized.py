class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0,
        }

        for char in text:
            if char in balloon:
                balloon[char] += 1

        balloon["l"] = balloon["l"] // 2
        balloon["o"] = balloon["o"] // 2

        return min(balloon["b"], balloon["a"], balloon["l"], balloon["o"], balloon["n"])


print(Solution().maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
