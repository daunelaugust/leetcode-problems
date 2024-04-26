def containsDuplicate(self, nums: List[int]) -> bool:
    # init hashmap, store numbers in a set for less memory usage!!!
    #amortized O(1) look up by hashing
    map = {}

    #loop through array
    for i in range(len(nums)):
        #if we seen any of the elements before return false
        if nums[i] in map:
            return True
        else:
            map[nums[i]] = i

    
    return False