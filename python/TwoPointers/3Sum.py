def threeSum(self, nums: List[int]) -> List[List[int]]:

    newNums = sorted(nums)
    print(newNums)
    maps = []

    for i in range(len(newNums)):

        if i > 0 and newNums[i] == newNums[i-1]:
            continue
        j= i+1
        k = len(newNums)-1
        
        while j<k:
            if (newNums[i] + newNums[j] + newNums[k])<0:
                j+=1
            elif (newNums[i] + newNums[j] + newNums[k])>0:
                k-=1
            else:
                maps.append([newNums[i], newNums[j], newNums[k]])
                k-=1
                while newNums[k] == newNums[k+1] and k>0:
                    k-=1
            
            
            

    
    return maps
