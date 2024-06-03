def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # horizontal solution
        horiz = set()
        board_map = defaultdict(list)
        # vertical solution
        vert_map = defaultdict(list)
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                print(vert_map[j])
                if j in vert_map:
                    if board[i][j] in vert_map[j]:
                        return False
                vert_map[j].append (board[i][j])
                if board[i][j] in horiz:
                    return False
                horiz.add(board[i][j])
            horiz = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                x = i//3
                y = j//3
                pair = (x,y)
                if pair in board_map:
                    if board[i][j] in board_map[pair]:
                        return False
                    board_map[pair].append(board[i][j])
                board_map[pair].append(board[i][j])
                
                
        return True

            