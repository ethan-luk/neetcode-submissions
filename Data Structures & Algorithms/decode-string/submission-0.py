class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        # 1. char is an integer
        # 2. char is a letter
        # 3. char is an open bracket
        # 4. char is a closed bracket
    
        # (2, [, a, 3, [, b, ])

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                curString = ""
                while stack[-1] != "[":
                    curString = stack.pop() + curString
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * curString)

        return "".join(stack)