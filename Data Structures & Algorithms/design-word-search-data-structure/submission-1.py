class TrieNode: 
    def __init__(self): 
        self.children = {} 
        self.end = False 


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        
        for w in word: 
            if w not in curr.children: 
                curr.children[w] = TrieNode() 
            curr = curr.children[w]
        
        curr.end = True
        
    def search(self, word: str) -> bool:

        curr = self.root

        def dfs(trie, i): 
            if i == len(word):
                return trie.end 
            
            char = word[i]

            if char != '.': 
                if char not in trie.children:   # changed curr -> trie
                    return False
                else:
                    return dfs(trie.children[char], i + 1)
            
            else: 
                for child in trie.children.values():   # changed curr -> trie
                    if dfs(child, i + 1):
                        return True 

            return False 
        
        return dfs(curr, 0)