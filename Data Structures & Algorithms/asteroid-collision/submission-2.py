class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            alive = True
            while alive and ast < 0 and stack and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()      # top destroyed, keep checking
                    continue
                elif stack[-1] == -ast:
                    stack.pop()      # both destroyed
                alive = False        # ast destroyed (or mutual destruction handled above)

            if alive:
                stack.append(ast)

        return stack