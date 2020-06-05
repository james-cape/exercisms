class Solution:
    def get_divide(self, matrix):
        if not matrix:
            return []

        number_rows = len(matrix)
        number_columns = len(matrix[0])

        pacific_board = []
        atlantic_board = []
        # Create empty board of 0s (and 1s for Pacific border)
        for x in range(number_rows):
            pacific_row = []
            atlantic_row = []
            for y in range(number_columns):
                if x == 0 or y == 0:
                    pacific_row.append(1)
                else:
                    pacific_row.append(0)
                if x == number_rows - 1 or y == number_columns - 1:
                    atlantic_row.append(1)
                else:
                    atlantic_row.append(0)
            pacific_board.append(pacific_row)
            atlantic_board.append(atlantic_row)

        # Set Pacific coordinates
        revisit = []
        for x in range(number_rows):
            for y in range(number_columns):
                if pacific_board[x][y] == 1:
                    self.add_higher_neighbors_to_board(x, y, matrix, pacific_board, revisit)
                    while revisit:
                        revisit_x = revisit[0][0]
                        revisit_y = revisit[0][1]
                        revisit.pop(0)
                        self.add_higher_neighbors_to_board(revisit_x, revisit_y, matrix, pacific_board, revisit)
        
        # Atlantic coordinates
        revisit = []
        for x in range(number_rows-1, -1, -1):
            for y in range(number_columns-1, -1, -1):
                if atlantic_board[x][y] == 1:
                    self.add_higher_neighbors_to_board(x, y, matrix, atlantic_board, revisit)
                    while revisit:
                        revisit_x = revisit[0][0]
                        revisit_y = revisit[0][1]
                        revisit.pop(0)
                        self.add_higher_neighbors_to_board(revisit_x, revisit_y, matrix, atlantic_board, revisit)

        continental_divide = []
        for row in range(number_rows):
            for column in range(number_columns):
                if pacific_board[row][column] == 1 and atlantic_board[row][column] == 1:
                    continental_divide.append([row, column])
        return continental_divide
        
    def add_higher_neighbors_to_board(self, x, y, matrix, board, revisit):
        number_rows = len(matrix)
        number_columns = len(matrix[0])

        if x+1 in range(number_rows): 
            if board[x+1][y] == 0:                
                if matrix[x+1][y] >= matrix[x][y]:
                    board[x+1][y] = 1
                    revisit.append([x+1, y])
        
        if x-1 in range(number_rows):
            if board[x-1][y] == 0:
                if matrix[x-1][y] >= matrix[x][y]:
                    board[x-1][y] = 1
                    revisit.append([x-1, y])
        
        if y+1 in range(number_columns):
            if board[x][y+1] == 0:
                if matrix[x][y+1] >= matrix[x][y]:
                    board[x][y+1] = 1
                    revisit.append([x, y+1])
        
        if y-1 in range(number_columns):
            if board[x][y-1] == 0:
                if matrix[x][y-1] >= matrix[x][y]:
                    board[x][y-1] = 1
                    revisit.append([x, y-1])
