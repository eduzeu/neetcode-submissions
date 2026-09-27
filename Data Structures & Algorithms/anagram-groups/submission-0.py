class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for st in strs: 
            key = ''.join(sorted(st))
            if key not in anagrams: 
                anagrams[key] = [st]
            else:
                anagrams[key].append(st)
    
        return anagrams.values()
         
        