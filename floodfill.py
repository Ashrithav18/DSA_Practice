def floodFill(image, sr, sc, color):
    rows = len(image)
    cols = len(image[0])
    
    original = image[sr][sc]
    
    # If already same color → no change
    if original == color:
        return image
    
    def dfs(r, c):
        # Check boundaries
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        
        # Only fill same color
        if image[r][c] != original:
            return
        
        # Change color
        image[r][c] = color
        
        # Move in 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    dfs(sr, sc)
    return image


# Function Call
image = [[1,1,1],[1,1,0],[1,0,1]]
print(floodFill(image, 1, 1, 2))