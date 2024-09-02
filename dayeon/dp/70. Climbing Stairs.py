# Solution 1

# Time O(n)
# Space O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1

        dp = 1

        for _ in range(2, n+1):
            dp = prev1 + prev2
            prev1 = prev2
            prev2 = dp
        
        return dp

# Solution 2

# Time O(n)
# Space O(n)
class Solution:
  def climbStairs(self, n: int) -> int:
    # dp[i] := the number of ways to climb to the i-th stair
    dp = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
