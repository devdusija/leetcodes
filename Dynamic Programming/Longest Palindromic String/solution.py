class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1 #all single letters are palindrome
        start = 0
        max_len = 1
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = l + i - 1
                if s[i] == s[j]:
                    if l == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                    if dp[i][j] and l > max_len:
                        start = i
                        max_len = l

        return s[start:start + max_len]