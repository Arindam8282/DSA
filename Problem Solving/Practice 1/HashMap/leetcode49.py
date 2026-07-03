def groupAnagrams(strs: [str]) -> [[str]]:
    existKeys = {}
    for key in strs:
        sortKey = "".join(sorted(key))
        if sortKey in existKeys:
            existKeys[sortKey].append(key)
        else:
            existKeys[sortKey] = [key]
    return list(existKeys.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["a"]))
print(groupAnagrams([""]))

