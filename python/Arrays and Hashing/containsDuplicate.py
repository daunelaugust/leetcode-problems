def containsDuplicate(self, nums: List[int]) -> bool:
    # # init a map
    # counter = {}
    # #loop through list
    # for i in nums:

    #     # if element exist in map return true
    #     if i in counter:
    #         return True
    #     #count of 1 in map for an elemnt that is found
    #     counter[i] = 1
    # #if we complete the entire loop without returning true then all elements are distinct
    # return False  
    # # another way to solve this is comparing length ofd the inout list as a set with the length of the list for a faster runtime

    #redo 07/28/24
    if len(set(nums)) != len(nums):
        return True
    else:
        return False