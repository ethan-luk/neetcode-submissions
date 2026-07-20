class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                one = stack.pop()
                two = stack.pop()
                if token == "+":
                    stack.append(one + two)
                elif token == "-":
                    stack.append(two - one)
                elif token == "*":
                    stack.append(one * two)
                elif token == "/":
                    stack.append(int(two / one))
        
        return stack[-1]