class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        i = -1
        c = 0
        for i in range(-1,-n-1,-1):
            if s[i] == " " :
                break
            c+=1
        return c        