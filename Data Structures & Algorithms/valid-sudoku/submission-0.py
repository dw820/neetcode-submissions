class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def hasDupe(l_s: List[str]) -> bool:
            s = set()

            for string in l_s:
                if string == '.':
                    continue
                if string in s:
                    return True
                s.add(string)
            
            return False


        for i in range(9):
            if hasDupe(board[i]):
                return False

            col = [board[j][i] for j in range(9)]
            if hasDupe(col):
                return False


        for i in range(0,9,3):
            for j in range(0,9,3):
                box = []
                for r in range(i, i+3):
                    box.extend(board[r][j:j+3])
                if hasDupe(box):
                    return False
        
        return True
                
        
        