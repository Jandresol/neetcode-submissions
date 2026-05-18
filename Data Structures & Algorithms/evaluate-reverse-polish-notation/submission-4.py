class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                subtractend, minuend = stack.pop(), stack.pop()
                stack.append(minuend - subtractend)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                divisor, dividend = stack.pop(), stack.pop()
                stack.append(int(float(dividend) / divisor))
            else:
                stack.append(int(token))
        return stack.pop()

        