class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        try:
            stack = []
            for i in tokens:
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                elif i == "-":
                    sub = stack.pop()
                    stack.append(stack.pop() - sub)
                elif i == "*":
                    stack.append(stack.pop() * stack.pop())
                elif i == "/":
                    dsor = stack.pop()
                    dend = stack.pop()
                    neg = False
                    if (dsor < 0 and dend > 0) or (dsor > 0 and dend < 0):
                        neg = True
                    res = abs(dend) // abs(dsor)
                    if neg:
                        stack.append(-res)
                    else:
                        stack.append(res)
                else:
                    stack.append(int(i))
            return stack[-1]
        except IndexError:
            return None
        