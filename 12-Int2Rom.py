class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        romanN = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X",  5: "V", 1: "I"}
        romanNogg = {1000: "M", 100: "C", 10: "X",  1: "I"}
        for i in range(len(str(num)), 0, -1):
            t = num // 10 ** (i - 1) % 10
            tt = t * (10 ** (i - 1))
            if t != 4 and t != 9:
                while tt > 0:
                    for j in romanN:
                        if tt - j >= 0:
                            tt -= j
                            res += romanN[j]
                            break
            else:
                last = ""
                if t == 4:
                    tz = romanN
                else:
                    tz = romanNogg
                for j in tz:
                    if tt - j > 0:
                        res += (tz[j] + last)
                        break
                    last = tz[j]
        return res
