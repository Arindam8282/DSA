def maxArea(height) -> int:
    l = 0
    r = len(height)-1
    maxl = height[l]*height[r]
    maxr = height[r]*height[l]
    maxdis = 0
    maxval = 0
    out = 0
    while l<r:
        if height[l]>height[r]:
            if(maxr<=(height[r]*height[l])):
                maxr = height[r]*height[l]
                if(maxdis<(l-r)):
                    maxdis = l-r
                if(maxval<maxr):
                    maxval = maxr
                out = height[r]**2
            r -= 1
        else:
            if(maxl<=(height[r]*height[l])):
                maxl = height[r]*height[l]
                if(maxdis<(r-l)):
                    maxdis = r-l
                if(maxval<maxl):
                    maxval = maxl
                out = height[l]**2
            l += 1

    print(maxdis,maxval,out)
    
maxArea([1,8,6,2,5,4,8,3,7])

        