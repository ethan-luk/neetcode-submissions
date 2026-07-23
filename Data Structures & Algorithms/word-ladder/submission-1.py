class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        words, res = set(wordList), 0
        q = deque([beginWord])

        def offByOne(one, two):
            diff = 0
            for i in range(len(one)):
                if one[i] != two[i]:
                    diff += 1
            return diff == 1

        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for word in list(words):
                    if offByOne(word, node):
                        q.append(word)
                        words.remove(word)
                    
        return 0
