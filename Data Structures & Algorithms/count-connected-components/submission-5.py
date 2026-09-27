class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {}
        if not edges:
            return n
            
        for n1, n2 in edges: 
            if n1 not in graph: 
                graph[n1] = []
            if n2 not in graph: 
                graph[n2] = []
            
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node, visit):
            visit.add(node)

            #explore all neighboors of current node

            for n in graph.get(node, []): 
                if n not in visit: 
                    dfs(n, visit)
        
        visit = set() 
        connected_components = 0 
        for n in range(n):
            if n not in visit: 
                dfs(n, visit)
                connected_components += 1

        return connected_components
  