class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack:
                if temperatures[i] >= stack[-1][0]:
                    stack.pop()
                else:
                    result[i] = stack[-1][1] - i
                    stack.append([temperatures[i], i])
                    break
    
            if not stack:
                result[i] = 0
                stack.append([temperatures[i], i])
        return result

