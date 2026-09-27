class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        letters = {}

        for i in range(len(s)):
            letters[s[i]] = i
        
        start = 0
        end = 0 
        partitions= []
        for i in range(len(s)):
            end = max(end, letters[s[i]])

            if i == end: 
                partitions.append(end - start + 1)
                start = i + 1
        
        return partitions
