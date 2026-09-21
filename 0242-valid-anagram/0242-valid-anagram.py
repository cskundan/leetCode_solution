class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = list(s)
        lst2 = list(t)
        lst1.sort()
        lst2.sort()
        r1 = "".join(lst1)
        r2 = "".join(lst2)
        if r1 == r2:
            return True
        else:
            return False