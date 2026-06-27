from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                else:
                    #checks row
                    if num in row[i]:
                        return False
                    else:
                        row[i].add(num)
                    #checks col
                    if num in col[j]:
                        return False
                    else:
                        col[j].add(num)
                    #checks box
                    key = tuple([i//3, j//3])
                    if num in box[key]:
                        return False
                    else:
                        box[key].add(num)
        return True
                    