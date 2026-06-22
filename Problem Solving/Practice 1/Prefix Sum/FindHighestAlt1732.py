def largestAltitude(gain: [int]) -> int:
    prefixList = [0]
    for i in range(len(gain)):
        prefixList.append(prefixList[i]+gain[i])
    return max(prefixList)

print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))
