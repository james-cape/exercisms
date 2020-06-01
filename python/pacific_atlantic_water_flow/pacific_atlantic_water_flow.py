# class Solution:
#     def get_divide(self, matrix):
#         if not matrix:
#             return []
#         # Set initial hashes of pacific and atlantic:
#         number_rows = len(matrix)
#         number_columns = len(matrix[0])
#         pacific = {'name': 'pacific'}
#         atlantic = {'name': 'atlantic'}
#         revisit = []

#         self.set_initial_ocean_coordinates(matrix, pacific, atlantic)


#         # Starting with pacific corner
#         for x in range(number_rows):
#             for y in range(number_columns):
#                 self.assign_ocean_if_connected(x, y, pacific, revisit, matrix)


#         # Starting with atlantic corner
#         for x in range(number_rows-1, -1, -1):
#             for y in range(number_columns-1, -1, -1):
#                 # Check for pacific connection
#                 self.assign_ocean_if_connected(x, y, atlantic, revisit, matrix)

#         return self.find_divide(pacific, atlantic)

#     def assign_ocean_if_connected(self, x, y, ocean, revisit, matrix):
#         if f'{x}, {y}' not in ocean:
#             number_rows = len(matrix)
#             number_columns = len(matrix[0])
#             # If so, add x,y to ocean hash (because it can flow down)
#             # Checks for any neighbor 1) on board, 2) flows to ocean, and 3) lower or equal to x,y elevation
#             if (
#                 x+1 in range(number_rows) and f'{x+1}, {y}' in ocean and matrix[x][y] >= matrix[x+1][y] or
#                 x-1 in range(number_rows) and f'{x-1}, {y}' in ocean and matrix[x][y] >= matrix[x-1][y] or
#                 y+1 in range(number_columns) and f'{x}, {y+1}' in ocean and matrix[x][y] >= matrix[x][y+1] or
#                 y-1 in range(number_columns) and f'{x}, {y-1}' in ocean and matrix[x][y] >= matrix[x][y-1]
#             ):
#                 ocean[f'{x}, {y}'] = matrix[x][y]



    #     # Add to revisit queue where flow goes unknown further elevations
    #     # If 1) on matrix, 2) higher/equal to upcoming elevation, 3) not in ocean
    #     # if (
    #     #     ocean['name'] == 'pacific' and
    #     #     y+1 in range(number_columns-1) and 
    #     #     matrix[x][y] >= matrix[x][y+1] and 
    #     #     f'{x}, {y+1}' not in ocean
    #     # ) or (
    #     #     ocean['name'] == 'atlantic' and
    #     #     y-1 in range(number_columns-1) and 
    #     #     matrix[x][y] >= matrix[x][y-1] and 
    #     #     f'{x}, {y-1}' not in ocean
    #     # ):
    #     #     revisit.append([x, y])
        



    # def set_initial_ocean_coordinates(self, matrix, pacific, atlantic):
    #     number_rows = len(matrix)
    #     number_columns = len(matrix[0])

    #     for y in range(number_columns):
    #         # Top row
    #         pacific[f'0, {y}'] = matrix[0][y]
    #         # Bottom row
    #         atlantic[f'{number_rows-1}, {y}'] = matrix[number_rows-1][y]
        
    #     for x in range(number_rows):
    #         # Left column
    #         pacific[f'{x}, 0'] = matrix[x][0]
    #         # Right column
    #         atlantic[f'{x}, {number_columns-1}'] = matrix[x][number_columns-1]

    # def find_divide(self, pacific, atlantic):
    #     continental_divide = []
    #     for key in list(pacific.keys()):
    #         if key != 'name' and key in atlantic:
    #             continental_divide.append([int(x) for x in key.split(', ')])
    #     return continental_divide





class Solution:
    def get_divide(self, matrix):
        if not matrix:
            return []
        # Set initial hashes of pacific and atlantic:
        number_rows = len(matrix)
        number_columns = len(matrix[0])
        pacific = {}
        atlantic = {}

        self.set_initial_ocean_coordinates(matrix, pacific, atlantic)

        all_mapped = False
        while not all_mapped:
            all_mapped = True
            # Starting with pacific corner
            for x in range(number_rows):
                for y in range(number_columns):
                    if f'{x}, {y}' not in pacific:
                        # Check if elevation is higher or equal to any n/s/e/w neighbors in pacific hash
                        # If so, add x,y to pacific hash (because it can flow down)
                        if self.flows_into_ocean(x, y, matrix, ocean=pacific):
                            all_mapped = False
                            pacific[f'{x}, {y}'] = matrix[x][y]

            # Starting with atlantic corner
            for x in range(number_rows-1, -1, -1):
                for y in range(number_columns-1, -1, -1):
                    # Check for pacific connection
                    if f'{x}, {y}' not in atlantic:
                        # Check if elevation is higher or equal to any n/s/e/w neighbors in atlantic hash
                        # If so, add x,y to atlantic hash (because it can flow down)
                        if self.flows_into_ocean(x, y, matrix, ocean=atlantic):
                            all_mapped = False
                            atlantic[f'{x}, {y}'] = matrix[x][y]

        return self.find_divide(pacific, atlantic)


    def flows_into_ocean(self, x, y, matrix, ocean):
        # Checks for any neighbor 1) on board, 2) flows to ocean, and 3) lower or equal to x,y elevation
        return (
            x+1 in range(len(matrix)) and f'{x+1}, {y}' in ocean and matrix[x][y] >= matrix[x+1][y] or
            x-1 in range(len(matrix)) and f'{x-1}, {y}' in ocean and matrix[x][y] >= matrix[x-1][y] or
            y+1 in range(len(matrix[0])) and f'{x}, {y+1}' in ocean and matrix[x][y] >= matrix[x][y+1] or
            y-1 in range(len(matrix[0])) and f'{x}, {y-1}' in ocean and matrix[x][y] >= matrix[x][y-1]
        )



    def set_initial_ocean_coordinates(self, matrix, pacific, atlantic):
        number_rows = len(matrix)
        number_columns = len(matrix[0])

        for y in range(number_columns):
            # Top row
            pacific[f'0, {y}'] = matrix[0][y]
            # Bottom row
            atlantic[f'{number_rows-1}, {y}'] = matrix[number_rows-1][y]
        
        for x in range(number_rows):
            # Left column
            pacific[f'{x}, 0'] = matrix[x][0]
            # Right column
            atlantic[f'{x}, {number_columns-1}'] = matrix[x][number_columns-1]

    def find_divide(self, pacific, atlantic):
        continental_divide = []
        for key in list(pacific.keys()):
            if key in atlantic:
                continental_divide.append([int(x) for x in key.split(', ')])
        return continental_divide







# class Solution:
#     def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
#         if not matrix:
#             return []
#         # Set initial hashes of pacific and atlantic:
#         number_rows = len(matrix)
#         number_columns = len(matrix[0])
#         pacific = {}
#         atlantic = {}

#         self.set_initial_ocean_coordinates(matrix, pacific, atlantic)

#         all_mapped = False
#         while not all_mapped:
#             all_mapped = True
#             # Starting with pacific corner
#             for x in range(number_rows):
#                 for y in range(number_columns):
#                     if f'{x}, {y}' not in pacific:
#                         # Check if elevation is higher or equal to any n/s/e/w neighbors in pacific hash
#                         # If so, add x,y to pacific hash (because it can flow down)
#                         if self.flows_into_ocean(x, y, matrix, ocean=pacific):
#                             all_mapped = False
#                             pacific[f'{x}, {y}'] = matrix[x][y]

#             # Starting with atlantic corner
#             for x in range(number_rows-1, -1, -1):
#                 for y in range(number_columns-1, -1, -1):
#                     # Check for pacific connection
#                     if f'{x}, {y}' not in atlantic:
#                         # Check if elevation is higher or equal to any n/s/e/w neighbors in atlantic hash
#                         # If so, add x,y to atlantic hash (because it can flow down)
#                         if self.flows_into_ocean(x, y, matrix, ocean=atlantic):
#                             all_mapped = False
#                             atlantic[f'{x}, {y}'] = matrix[x][y]

#         return self.find_divide(pacific, atlantic)


#     def flows_into_ocean(self, x, y, matrix, ocean):
#         # Checks for any neighbor 1) on board, 2) flows to ocean, and 3) lower or equal to x,y elevation
#         return (
#             x+1 in range(len(matrix)) and f'{x+1}, {y}' in ocean and matrix[x][y] >= ocean[f'{x+1}, {y}'] or
#             x-1 in range(len(matrix)) and f'{x-1}, {y}' in ocean and matrix[x][y] >= ocean[f'{x-1}, {y}'] or
#             y+1 in range(len(matrix[0])) and f'{x}, {y+1}' in ocean and matrix[x][y] >= ocean[f'{x}, {y+1}'] or
#             y-1 in range(len(matrix[0])) and f'{x}, {y-1}' in ocean and matrix[x][y] >= ocean[f'{x}, {y-1}']
#         )

#     def set_initial_ocean_coordinates(self, matrix, pacific, atlantic):
#         number_rows = len(matrix)
#         number_columns = len(matrix[0])

#         for y in range(number_columns):
#             # Top row
#             pacific[f'0, {y}'] = matrix[0][y]
#             # Bottom row
#             atlantic[f'{number_rows-1}, {y}'] = matrix[number_rows-1][y]
        
#         for x in range(number_rows):
#             # Left column
#             pacific[f'{x}, 0'] = matrix[x][0]
#             # Right column
#             atlantic[f'{x}, {number_columns-1}'] = matrix[x][number_columns-1]

#     def find_divide(self, pacific, atlantic):
#         continental_divide = []
#         for key in list(pacific.keys()):
#             if key in atlantic:
#                 continental_divide.append([int(x) for x in key.split(', ')])
#         return continental_divide