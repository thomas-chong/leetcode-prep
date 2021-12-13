class Solution:
    def fib(self, n: int) -> int:
        results = []
        for i in range(0, n+1):
            if i == 0:
                results.append(0)
            elif i == 1:
                results.append(1)
            else:
                results.append(results[i-1] + results[i-2])
        
        return results[n]