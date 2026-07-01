class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: # O(N^2) solution
        nr = len(board)
        if not nr:
            return True
        nc = len(board[1])

        for r in range(nr): # Column check
            d = {}
            for c in range(nc):
                element = board[r][c]
                if element != ".":
                    if element in d:
                        print("Column check failed")
                        # print("Column check failed at row, column:", r, c)
                        # print(d)
                        return False
                    d[board[r][c]] = 1
        
        for c in range(nc): # Row check
            d = {}
            for r in range(nr):
                element = board[r][c]
                if element != ".":
                    if element in d:
                        print("Row check cleared")
                        return False
                    d[board[r][c]] = 1

        # Square check
        for smr in range(0, 8, 3):
            for smc in range(0, 8, 3):
                d = {}
                for r in range(3):
                    for c in range(3):
                        element = board[smr + r][smc + c]
                        if element != ".":
                            if element in d:
                                print("Square check cleared")
                                return False
                            d[board[smr + r][smc + c]] = 1

        return True