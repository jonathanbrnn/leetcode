class Solution:
    def numberOfLines(self, width: List[int], s: str) -> List[int]:
        pix = 0
        line = 1
        i = 0
        a = 97
        while i<len(s):
            if pix<=100:
                pix+=width[ord(s[i])-a]
                i+=1
                if pix>100:
                    line+=1
                    pix=0
                    i-=1
        return [line, pix]
