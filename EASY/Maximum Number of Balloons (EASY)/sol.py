from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = 10**5
        cou = Counter(text)
        cur = ""
        if len(text) < 6 or text.count("o") < 2:
            return 0
        for item, val in cou.items():
            if item in "baloon":
                print(item, val)
                if item == "o":
                    res = min(val//2, res)
                elif item == "l":
                    res = min(val//2, res)
                else:
                    res = min(val, res)
                if item not in cur:
                    cur += item
        return res if len(cur) == 5 else 0


print(Solution().maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
