class TrieNode: 
    def __init__(self):
        self.children = {}
        self.fullWord = False

    def addWord(self, word):
        curr = self
        for c in word:    
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.fullWord = True    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        #make trie
        for w in words: 
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or r >= rows or c < 0 or c >= cols or  (r,c) in visit or board[r][c] not in node.children or board[r][c] == "#":
                return 
            
            temp = board[r][c] 
            board[r][c] = "#"
            node = node.children[temp]
            word += temp

            if node.fullWord:
                res.add(word)

            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dx, dy in directions:
                dfs(dx + r, dy + c, node, word)

            board[r][c] = temp #unmark
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")

        return list(res)
            

