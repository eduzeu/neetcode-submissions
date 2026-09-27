class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

      
        if not edges:
            return True

        #run DFS to visit all nodes
        #have set to keep track of visited nodes in current run
        #if something in set, then cyclye detected

        #create graph with format n: [neigboors]
        graph = {}
        for n1, n2 in edges: 
            if n1 not in graph:
                graph[n1] = []
            if n2 not in graph:
                graph[n2] = []
            graph[n1].append(n2)
            graph[n2].append(n1)

        visit = set()

        def dfs(node, parent):
            if node in visit: 
                return False
            
            visit.add(node)

            for n in graph[node]:
                if n != parent:
                    if not dfs(n, node):
                        return False
        
            return True 
        
        return dfs(0, None) and len(visit) == n
