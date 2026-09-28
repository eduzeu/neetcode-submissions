class TrieNode: 
    def __init__(self): 
        self.children = {} 
        self.end = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        found_words = set()

        rows, cols = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        root = TrieNode() 

        # Build Trie
        for word in words: 
            curr = root 

            for c in word: 
                if c not in curr.children: 
                    curr.children[c] = TrieNode()

                curr = curr.children[c]
            
            curr.end = word 
        

        def dfs(r, c, trie): 
            char = board[r][c] 

            if char not in trie.children:
                return 
            
            next_char = trie.children[char]

            # Found a word
            if next_char.end: 
                found_words.add(next_char.end)
            
            # Mark visited
            board[r][c] = "#"
            
            for dx, dy in directions: 
                nr, nc = r + dx, c + dy

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] != "#"
                ):
                    dfs(nr, nc, next_char)
            
            # Backtrack
            board[r][c] = char
                

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)


        return list(found_words)