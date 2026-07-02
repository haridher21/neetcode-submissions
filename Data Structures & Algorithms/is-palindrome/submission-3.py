class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c
        n = len(new_s)
        new_s = new_s.lower()
        for i in range(n // 2):
            if new_s[i] != new_s[n - i - 1]:
                return False
        return True