class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = {}
        for i in s:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
                if res[i] == 2:
                    return i
        return None
