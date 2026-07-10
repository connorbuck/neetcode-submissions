class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = -float("inf")
        L = 0

        substr = ""
        for R in range(len(s)):
            while s[R] in substr:
                substr = substr[1:]
                L = L + 1

            substr += s[R]
            length = max(length, len(substr))
        if length == -float("inf"): return 0
        return length
