class Solution:
    def numIslands(self, grid):
        counter = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    counter += 1
                    self.search_land([[x, y]], grid)
        return counter

    def search_land(self, land_mass, grid):
        if land_mass:
            x = land_mass[0][0]
            y = land_mass[0][1]
            x_range = range(len(grid[0]))
            y_range = range(len(grid))
            grid[y][x] = '0'
            land_mass.pop(0)
            if (y+1) in y_range and grid[y+1][x] == '1':
                if [x, y+1] not in land_mass:
                    land_mass.append([x, y+1])
            if (y-1) in y_range and grid[y-1][x] == '1':
                if [x, y-1] not in land_mass:
                    land_mass.append([x, y-1])
            if (x+1) in x_range and grid[y][x+1] == '1':
                if [x+1, y] not in land_mass:
                    land_mass.append([x+1, y])
            if (x-1) in x_range and grid[y][x-1] == '1':
                if [x-1, y] not in land_mass:
                    land_mass.append([x-1, y])
            self.search_land(land_mass, grid)

# Make BFS without recursion
# Would just replace the land_mass appends with the search_land
# Could also make a while loop (while land_mass != []) and avoid recursion

            # For each cell in grid (left to right, top to bottom):
                # Find land
                # Iterate counter once
                # Run recursive function
                # Recursive function takes in array of coordinates [[x, y]]
                # If there are elements in the array:
                    # Recursive function turns first coordinate in array to 0 on the grid
                    # Recursive function removes first coordinate from array
                    # Recursive function appends coordinates to array which are neighbors and land
                    # Recursive function 
                    # Recursive function outputs vert/horiz neighbor coordinates which are land
                # If array is empty:
                    # Break out of recursive function. This should resume the search for another land.
            # Return counter
