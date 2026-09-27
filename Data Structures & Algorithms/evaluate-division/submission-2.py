from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:



        
        graph = defaultdict(list)

        for i, eq in enumerate(equations): 
            a, b = eq
            graph[a].append((b, values[i],))
            graph[b].append((a, 1/values[i]))
        
        def bfs(src, target):
            if src not in graph or target not in graph: 
                return -1.0 
            q = deque()
            q.append((src, 1))
            visited = set() 
            visited.add(src)

            while q: 

                curr_node, curr_val = q.popleft() 

                if curr_node == target: 
                    return curr_val 
                
                for nei, val in graph[curr_node]: 
                    if nei not in visited: 
                        q.append((nei, val * curr_val))
                        visited.add(nei)
            
            return -1.0
        
        return [bfs(a, b) for a, b in queries]
        