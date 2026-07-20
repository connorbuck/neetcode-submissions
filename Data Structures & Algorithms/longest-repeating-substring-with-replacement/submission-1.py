class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for char in set(s):
            L = 0
            max_replacements = k
            for R in range(len(s)):
                if s[R] != char:
                    max_replacements -= 1
                while max_replacements < 0:
                    if s[L] != char:
                        max_replacements += 1
                    L += 1
                res = max(res, R - L + 1)
        return res