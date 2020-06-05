class Solution:
    def get_divide(self, matrix):
        if not matrix:
            return []

        board_data = {
            'number_rows': len(matrix),
            'number_columns': len(matrix[0]),
            'pacific_board': [],
            'atlantic_board': [],
            'matrix': matrix,
            'revisit': []
        }

        # Create empty board of 0s (and 1s for Ocean border)
        for x in range(board_data['number_rows']):
            pacific_row = []
            atlantic_row = []
            for y in range(board_data['number_columns']):
                if x == 0 or y == 0:
                    pacific_row.append(1)
                else:
                    pacific_row.append(0)
                if x == board_data['number_rows'] - 1 or y == board_data['number_columns'] - 1:
                    atlantic_row.append(1)
                else:
                    atlantic_row.append(0)
            board_data['pacific_board'].append(pacific_row)
            board_data['atlantic_board'].append(atlantic_row)

        # Find cells that flow to either ocean
        self.set_ocean_board(board_data, True)
        self.set_ocean_board(board_data, False)

        continental_divide = []
        for row in range(board_data['number_rows']):
            for column in range(board_data['number_columns']):
                if board_data['pacific_board'][row][column] == 1 and board_data['atlantic_board'][row][column] == 1:
                    continental_divide.append([row, column])
        return continental_divide


    # Set Ocean coordinates
    def set_ocean_board(self, board_data, pacific=True):
        if pacific:
            x_range = range(board_data['number_rows'])
            y_range = range(board_data['number_columns'])
            ocean_board = board_data['pacific_board']
        else:
            x_range = range(board_data['number_rows']-1, -1, -1)
            y_range = range(board_data['number_columns']-1, -1, -1)
            ocean_board = board_data['atlantic_board']

        for x in x_range:
            for y in y_range:
                if ocean_board[x][y] == 1:
                    self.add_higher_neighbors_to_board(x, y, board_data, ocean_board)
                    while board_data['revisit']:
                        revisit_x = board_data['revisit'][0][0]
                        revisit_y = board_data['revisit'][0][1]
                        board_data['revisit'].pop(0)
                        self.add_higher_neighbors_to_board(revisit_x, revisit_y, board_data, ocean_board)
        

    def add_higher_neighbors_to_board(self, x, y, board_data, board):

        south = {'x': x+1, 'y': y}
        north = {'x': x-1, 'y': y}
        east = {'x': x, 'y': y+1}
        west = {'x': x, 'y': y-1}

        for n in [south, north, east, west]:
            if n['x'] in range(board_data['number_rows']) and n['y'] in range(board_data['number_columns']):
                if board[n['x']][n['y']] == 0:
                    if board_data['matrix'][n['x']][n['y']] >= board_data['matrix'][x][y]:
                        board[n['x']][n['y']] = 1
                        board_data['revisit'].append([n['x'], n['y']])
