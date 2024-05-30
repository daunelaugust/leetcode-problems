def productExceptSelf(self, nums: List[int]) -> List[int]:

    res = [1]*(len(nums))
    prefix = 1
    postfix = 1
    for i in range(len(nums)):
        if i == 0:
            res[i] = 1
            continue
        prefix = prefix * nums[i-1]
        res[i] = prefix

    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            postfix = postfix * nums[i]
            continue
        res[i] = postfix*res[i]
        postfix = postfix * nums[i]
    
    

    return res

        