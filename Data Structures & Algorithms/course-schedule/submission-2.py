class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        #treat like graph
        #if cycle is found then we can't do this 

        graph = {}

        for a, b in prerequisites: 
            if b not in graph: 
                graph[b] = [a]
            else: 
                graph[b].append(a)
        
        for i in range(numCourses):
            if i not in graph: 
                graph[i] = []

        visit = set()
        cycle = set() 
        def dfs(start):

            if start in cycle:
                return False #cycle found 
            
            if start in visit:
                return True 

            cycle.add(start)

            for n in graph[start]:
                if not dfs(n):
                    return False

            cycle.remove(start)
            visit.add(start)

            
            return True #no cycle found 
        
        for n in range(numCourses):
            if not dfs(n):
                return False

        return True 
 

        
        