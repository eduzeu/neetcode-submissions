class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        q = deque() 
        graph = defaultdict(list)
        steps = 0 
        visited = set() 
        q.append((beginWord, 0)) #word, steps
        visited.add(beginWord)
        
        #build graph 
        # *at -> cat, bat
        #c*t -? cat 
        # ca* -> cat

        #*ag -> bag, sag

        for word in wordList: 
            for i in range(len(word)): 
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)

        while q: 

            curr_word, steps = q.popleft() 

            if curr_word == endWord: 
                return steps  +1
            
            for i in range(len(curr_word)):
                pattern = curr_word[:i] + "*" + curr_word[i+1:]
                for nei in graph[pattern]: 
                    if nei not in visited: 
                        q.append((nei, steps +1))
                        visited.add(nei)
            
        return 0









        