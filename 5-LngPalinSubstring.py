class Solution:
    def longestPalindrome(self, s: str) -> str:
        lonPal = s[0]
        if len(s) == 1:
            return s
        for i in range(len(s) + 1, 1, -1):
            for j in range(0, len(s) - i + 1):
                ts = s[j:j+i]
                palindrom = True
                left = 0
                right = len(ts) - 1
                while palindrom and left < right:
                    if ts[left] != ts[right]:
                        palindrom = False
                        break
                    left += 1
                    right -= 1
                if palindrom and len(ts) > len(lonPal):
                    return(ts)
        return lonPal
