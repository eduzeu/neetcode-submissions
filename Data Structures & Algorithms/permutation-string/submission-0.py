class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #hashmap to count frequency and hashmap for s2
        freq = {}
        for char in s1: 
            freq[char] = freq.get(char, 0) + 1
        string = {}
        #window of size len(s1)
        window = len(s1)
        #iterate over s2
        for i in range(min(window, len(s2))):
            string[s2[i]] = string.get(s2[i], 0) + 1

        for i in range(window, len(s2)):
        #increment frequency 
            if string == freq:
                return True 

            string[s2[i]] = string.get(s2[i], 0) + 1
            
            left = s2[i - window]
            string[left] -= 1
            if string[left]== 0:
                del string[left]
        #increment/decrement frequency of s2 

        return True if freq == string else False

        