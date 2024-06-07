def twoSum(self, nums: List[int], target: int) -> List[int]:
    #init map
    maps={}

    #loop through the list
    for i in range(len(nums)):

        #calculate the difference for each element
        diff = target - nums[i]

        #check if difference exist already in map
        if diff in maps:
            # if it exist return the index of the element where the correct diff was found and the current position 
            return [maps[diff], i]
        
        #store current number as key  with index as value
        maps[nums[i]] = i