class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        arrays = []
        candidates.sort()

        def dfs(i, path, curr):
            if curr == target: 
                arrays.append(path.copy())
                return 
    
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx-1]:
                    continue 
                if curr + candidates[idx] > target:
                    break
                path.append(candidates[idx])
                dfs(idx+1, path , curr + candidates[idx])
                path.pop()
        
        dfs(0,[], 0)

        return arrays
            

        