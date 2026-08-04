class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        q = deque()
        q.append("0000")
        visited = set(["0000"])

        num_moves = 0
        while q:
            length = len(q)
            for _ in range(length):
                comb = q.popleft()
                if comb == target:
                    return num_moves
                for i in range(len(comb)):
                    # add one
                    new_c = str((int(comb[i]) + 1) % 10)
                    new_comb = comb[:i] + new_c + comb[i+1:]
                    if new_comb not in deadends and new_comb not in visited:
                        visited.add(new_comb)
                        q.append(new_comb)

                    # subtract one
                    new_c = str((int(comb[i]) - 1) % 10)
                    new_comb = comb[:i] + new_c + comb[i+1:]
                    if new_comb not in deadends and new_comb not in visited:
                        visited.add(new_comb)
                        q.append(new_comb)
            num_moves += 1
        return -1