class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:a+i]:
                return i
        return -1