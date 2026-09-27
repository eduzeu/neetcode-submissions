class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #make a graph with format: 
        #b: list of a courses 
        # [[0,1],[2,0],[]
        #1: 0, 0: 2

        graph = {}
        for a,b in prerequisites: 
            if b not in graph:
                graph[b] = []
             
            graph[b].append(a)

        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
                
        visit = set()        
        #run dfs and keep track of the visited courses 
        def dfs(course):

            #if we find a cycle (visited in current dfs) then we return false 
            if course in visit: 
                return False 

            if graph[course] == []: #no prereqs for this course
                return True 
            
            visit.add(course) #add current node to visited 

            for crs in graph[course]:
                if not dfs(crs):
                    return False 
            
            visit.remove(course)
            graph[course] = []
            return True 
            
        
        for c in range(numCourses): 
            if not dfs(c):
                return False

        return True
        