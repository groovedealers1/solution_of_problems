class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return 'false'
        else:
            a = enumerate(s)
            return next(a), next(a)

s = '()[]{}'
solution = Solution()
print(solution.isValid(s))