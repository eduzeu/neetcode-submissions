class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites: 
            graph[b].append(a)
        
        safe, cycle = set(), set()

        def dfs(node): 
            if node in safe:
                return True
            if node in cycle:
                return False
            
            cycle.add(node)

            for nei in graph[node]: 
                if not dfs(nei):
                    return False
            

            cycle.remove(node)
            safe.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True