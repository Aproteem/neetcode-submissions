from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_set = {"1","2","3","4","5","6","7","8","9","."}

        rows = defaultdict(set) #key = row index, value = set of the row
        cols = defaultdict(set) #key = col index, value = set of the col
        boxes = defaultdict(set) #key = tuple(row_i//3, col_i//3)

        for i in range(9):
            for j in range(9):
                if board[i][j] not in valid_set:
                    #validates each elememt
                    return false
                else:
                    elm = board[i][j]

                    if elm == ".":
                        #ignores empty places
                        continue
                    else:
                        #check and add to row_set
                        if elm in rows[i]:
                            return False
                        else:
                            rows[i].add(elm)

                        #check and add to col_set
                        if elm in cols[j]:
                            return False
                        else:
                            cols[j].add(elm)
                        
                        #check and add to boxes_set
                        key = tuple([i//3, j//3])
                        if elm in boxes[key]:
                            return False
                        else:
                            boxes[key].add(elm)
        return True


                    
                    
