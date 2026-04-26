def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w

        max_water = max(max_water, area)

        # Move the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Function Calls
print(maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(maxArea([1,1]))               # 1