class Solution:
    def get_divide(self, matrix):
        
        if not matrix:
            return []
                
        num_rows = len(matrix)
        num_cols = len(matrix[0])
            
        # DFS: continue to next cell if maintaining or increasing height
        def dfs(pacific: bool):
            flows_to = [[False] * num_cols for _ in range(num_rows)]
            # keep stack of (minHeight, coordinate) tuples
            # add all of first row and col to stack
            stack = []
            for row in range(num_rows):
                stack.append((0, (row, 0 if pacific else num_cols - 1)))
            for col in range(num_cols):
                stack.append((0, (0 if pacific else num_rows - 1, col)))
            breakpoint()
            while stack:
                # pop min_height and coordinates off
                min_height, (row, col) = stack.pop()
                
                # if off baord, continue
                if not 0 <= row < num_rows or not 0 <= col < num_cols:
                    continue
                
                # if height < minHeight or coordinate already marked True, continue
                height = matrix[row][col]
                if height < min_height or flows_to[row][col]:
                    continue
                    
                # mark as flows to the ocean
                flows_to[row][col] = True
                
                # else add all adjacent cells with minheight equal to current height
                for dRow, dCol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    stack.append((height, (row + dRow, col + dCol)))
                    
            return flows_to

        flows_to_pacific = dfs(pacific=True)
        flows_to_atlantic = dfs(pacific=False)
        
        ans = []
        
        # result will be intersection of both searches
        for row in range(num_rows):
            for col in range(num_cols):
                if flows_to_pacific[row][col] and flows_to_atlantic[row][col]:
                    ans.append([row, col])
                    
        return ans