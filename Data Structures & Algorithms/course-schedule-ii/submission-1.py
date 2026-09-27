class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = {c: [] for c in range(numCourses)}

        for a, b in prerequisites: 
            adjList[b].append(a)
        
        def dfs(start, seen, visiting, output):
            if start in visiting:
                return False

            if start in seen: 
                return True
                seen.add(start)
            
            visiting.add(start)

            for n in adjList[start]:
                if not dfs(n, seen, visiting, output):
                    return False
            
            visiting.remove(start)
            seen.add(start)
            output.append(start)
            return True
        
        seen, visiting = set(), set()
        output = []

        for c in range(numCourses):
            if not dfs(c, seen, visiting, output):
                return []

        return output[::-1]
                