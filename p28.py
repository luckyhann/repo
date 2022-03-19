class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i:len(needle)+i] == needle:
                    return i
