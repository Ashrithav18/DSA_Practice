def maxHeight(arr):

    arr.sort()

    prev_width = 0
    prev_count = 0

    curr_width = 0
    curr_count = 0

    height = 0

    for w in arr:

        curr_width += w
        curr_count += 1

        if curr_width > prev_width and curr_count > prev_count:
            height += 1
            prev_width = curr_width
            prev_count = curr_count
            curr_width = 0
            curr_count = 0

    return height


# Function Call
arr = [10,20,30,50,60,70]

print(maxHeight(arr))