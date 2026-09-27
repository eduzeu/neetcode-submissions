class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        #aproach
        #create adj list 
        #use dfs to calculate height of each node
        #keep the min height and the equal hegihts 
        #iterate thorguh it to check all nodes


        graph = {i: [] for i in range(n)}

        for a, b in edges: 
            graph[a].append(b)
            graph[b].append(a)
        

        def dfs(node, visit):
            
            visit.add(node)
            maxHeight = 0 
            for n in graph[node]:
                if n not in visit: 
                    hei = dfs(n, visit)
                    maxHeight = max(maxHeight, hei)
            return maxHeight + 1
        
        minHeight = float('inf')
        nodes = []
        #explore nodes
        for i in range(n):
            visit = set()
            hei = dfs(i, visit)
            if hei < minHeight: 
                minHeight = hei
                nodes = [i]
            elif hei == minHeight: 
                nodes.append(i)

        return nodes


        