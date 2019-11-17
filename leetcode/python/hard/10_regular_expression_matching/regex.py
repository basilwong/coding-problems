class Solution:

    def do_star(self, dp, i, j, temp, char):
        dp[i][j-1] = 1
        dp[i][j] = 1
        while (char == temp[j] or char == '.') and j < len(temp) - 1:
            dp[i][j+1] = 1
            j += 1

    def isMatch(self, s: str, p: str) -> bool:

        if not p and not s:
                return True
        elif not p:
            return False

        dp = [[0] * (len(s) + 1) for _ in range(len(p))]
        temp = s + '-'

        # first character
        if temp[0] == '-':
            dp[0][0] = -1
        elif temp[0] == p[0] or p[0] == '.':
            dp[0][1] = 1
        else:
            dp[0][0] = -1

        for i in range(1, len(p)):
            for j in range(len(temp)):

                if dp[i-1][j] == 0:
                    continue
                elif dp[i-1][j] == -1:
                    if p[i] == '*':
                        dp[i][j] = 1
                    continue

                if p[i] == temp[j] or p[i] == '.':
                    if temp[j] == '-':
                        if dp[i][j] != 1:
                            dp[i][j] = -1
                    else:
                        dp[i][j+1] = 1
                elif p[i] == '*':
                    if dp[i-1][j] == 1:
                        self.do_star(dp, i, j, temp, p[i-1])
                else:
                    if dp[i][j] != 1:
                        dp[i][j] = -1
                            
        return dp[len(p) - 1][len(s)] != 0 and dp[len(p) - 1][len(s)] != -1
