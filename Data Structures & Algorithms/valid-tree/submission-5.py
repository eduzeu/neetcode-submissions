class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

      
        if not edges:
            return True

        #run DFS to visit all nodes
        #have set to keep track of visited nodes in current run
        #if something in set, then cyclye detected

        #create graph with format n: [neigboors]
        graph = {i: [] for i in range(n)}

        for a, b in edges: 
            graph[a].append(b)
            graph[b].append(a) 

        visit = set()

        def dfs(node, parent):
            if node in visit: 
                return False
            
            visit.add(node)

            for n in graph[node]:
                if n == parent: 
                    continue
                else: 
                    if not dfs(n, node): #pass parent
                        return False
            
            return True

        return True if dfs(0, None) and len(visit) == n else False
           
