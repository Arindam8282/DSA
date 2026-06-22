def maxArea(height) -> int:
    l = 0
    r = len(height)-1
    max_area = 0
    while l<r:
        width = (r-l) * min(height[l],height[r])
        if max_area<width:
            max_area = width 
        if height[l]>height[r]:
            r -= 1
        else:
            l += 1
    print(max_area)
    return max_area
    
maxArea([1,1])

        