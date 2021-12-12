class Solution:
    def climbStairs(self, n: int) -> int:
        results = []
        for i in range(0,n):
            if i == 0:
                results.append(1)
            elif i == 1:
                results.append(2)
            else:
                results.append(results[i-1]+results[i-2])
        
        return results[n-1]