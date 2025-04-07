class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            x = s[i]
            if x not in countS:
                countS[x] = 1
            else:
                countS[x] = countS[x] + 1
            
            y = t[i]
            if y not in countT:
                countT[y] = 1
            else:
                countT[y] = countT[y] + 1
            
        return countS == countT
            
