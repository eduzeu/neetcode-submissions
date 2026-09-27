class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(set)
        visited = set()
        cycle = set()
        result = []

        for i in range(len(words)):
            if i == len(words) -1:
                break 
            if len(words[i]) > len(words[i+1]) and words[i].startswith(words[i+1]):
                return ""
            for j in range(min(len(words[i]), len(words[i+1]))):
            
                if words[i][j] == words[i+1][j]:
                    continue 
                else: 
                    graph[words[i][j]].add(words[i+1][j])
                    break

        #now run dfs on graph 
        def dfs(node):
            if node in visited: 
                return True
            if node in cycle:
                return False
            
            cycle.add(node)

            for n in graph[node]:
                if not dfs(n):
                    return False
            
            visited.add(node)
            cycle.remove(node)
            result.append(node)
            return True
        
        all_chars = set(''.join(words))
        for char in all_chars:
            graph.setdefault(char, set())

        for char in all_chars:
            if char not in visited:
                if not dfs(char):
                    return ""
        
        return ''.join(result[::-1])

        
                


        