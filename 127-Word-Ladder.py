class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbours = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                neighbours[word[:i] + "*" + word[i+1:]].append(word)
        q = deque()
        q.append(beginWord)
        visited = set([beginWord])
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count 
                for j in range(len(word)):
                    for n in neighbours[word[:j] + "*" + word[j+1:]]:
                        if n not in visited:
                            q.append(n)
                            visited.add(n)
            count += 1
        return 0
