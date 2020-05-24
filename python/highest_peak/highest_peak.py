class HighestPeak:
    def get_elevation(self, grid):
        elevation = -1
        # Get a queue of 0's
        old_lands = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    old_lands.append([x, y])

        # Go through the queue of 0s
        # Replace the queue with a new queue of 1s that touch 0s
        # Update old_lands queue and repeat until no lands
        while old_lands:
            new_lands = []
            for coordinate in old_lands:
                x = coordinate[0]
                y = coordinate[1]
                # Add to new_lands queue from coordinate's neighbors
                self.explore(x+1, y, grid, new_lands)
                self.explore(x-1, y, grid, new_lands)
                self.explore(x, y+1, grid, new_lands)
                self.explore(x, y-1, grid, new_lands)
            old_lands = new_lands
            elevation += 1
        return elevation

    def explore(self, x, y, grid, new_lands):
        if x in range(len(grid[0])) and y in range(len(grid)):
            if grid[y][x] == 1:
                # Set land to 0 and add to new_lands queue
                grid[y][x] = 0
                new_lands.append([x, y])








## Suboptimal
# class HighestPeak:
#     def get_elevation(self, grid):
#         counter = 1
#         land_exists = True

#         while land_exists == True:
#             land_exists = False
#             counter -= 1
#             for y in range(len(grid)):
#                 for x in range(len(grid[0])):
#                     if grid[y][x] == 1:
#                         land_exists = True
#                         self.explore_neighbors(x, y, grid, counter)
#         return abs(counter)


#     def explore_neighbors(self, x, y, grid, counter):
#         if self.on_grid(x, y+1, grid) and grid[y+1][x] == counter:
#             grid[y][x] = counter - 1
#         if self.on_grid(x, y-1, grid) and grid[y-1][x] == counter:
#             grid[y][x] = counter - 1
#         if self.on_grid(x+1, y, grid) and grid[y][x+1] == counter:
#             grid[y][x] = counter - 1
#         if self.on_grid(x-1, y, grid) and grid[y][x-1] == counter:
#             grid[y][x] = counter - 1

#     def on_grid(self, x, y, grid):
#         return x in range(len(grid[0])) and y in range(len(grid))




























    # grid = [
    #     [ 1,  1,  1,  0],
    #     [ 1,  1,  1,  1],
    #     [ 1,  1,  1,  1],
    #     [ 0,  0,  1,  1]
    # ]

    # # If point is land and point touches 0, turn to -1
    # grid = [
    #     [ 1,  1, -1,  0],
    #     [ 1,  1,  1, -1],
    #     [-1, -1,  1,  1],
    #     [ 0,  0, -1,  1]
    # ]

    # # If point is land and touches -1, turn to -2
    # grid = [
    #     [ 1, -2, -1,  0],
    #     [-2, -2, -2, -1],
    #     [-1, -1, -2, -2],
    #     [ 0,  0, -1, -2]
    # ]

    # # If point is land and touches -2, turn to -3
    # grid = [
    #     [-3, -2, -1,  0],
    #     [-2, -2, -2, -1],
    #     [-1, -1, -2, -2],
    #     [ 0,  0, -1, -2]
    # ]

    # # If no points == 1, return absolute value of counter

# # Worked until there was no water in the vertical or horizontal directions
# class HighestPeak:
#     def get_elevation(self, grid):
#         max_elevation = 0
#         for y in range(len(grid)):
#             for x in range(len(grid[0])):
#                 if grid[y][x] == 1:
#                     distance = self.distance_to_closest_water(x, y, 1, grid)
#                     if distance and distance > max_elevation:
#                         max_elevation = distance

#         return max_elevation

#     def distance_to_closest_water(self, x, y, distance_from_origin, grid):
#         if self.is_water(x, y-distance_from_origin, grid):
#             return distance_from_origin
#         if self.is_water(x, y+distance_from_origin, grid):
#             return distance_from_origin
#         if self.is_water(x+distance_from_origin, y, grid):
#             return distance_from_origin
#         if self.is_water(x-distance_from_origin, y, grid):
#             return distance_from_origin
#         distance_from_origin += 1
#         return self.distance_to_closest_water(x, y, distance_from_origin, grid)

#     def is_water(self, x, y, grid):
#         if x in range(len(grid[0])) and y in range(len(grid)):
#             return grid[y][x] == 0
#         else:
#             return False