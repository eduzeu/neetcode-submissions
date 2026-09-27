class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}
        
        for edge in edges: 
            n1, n2  = edge
            if n1 not in graph: 
                graph[n1] = []
            if n2 not in graph: 
                graph[n2] = []
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        
        def dfs(node, visit):
            visit.add(node)
            
            for n in graph.get(node, []):
                if n not in visit: 
                    dfs(n, visit)
                
        #if we have visited all nodes in component, add to count and move to other
        components = 0
        visit = set()
        
        for node in range(n):
            if node not in visit:
                dfs(node, visit)
                components += 1
        
        return components
        