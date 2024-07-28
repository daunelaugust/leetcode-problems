def productExceptSelf(self, nums: List[int]) -> List[int]:

    # res = [1]*(len(nums))
    # prefix = 1
    # postfix = 1
    # for i in range(len(nums)):
    #     res[i] = prefix
    #     prefix = prefix * nums[i]
        

    # for i in range(len(nums)-1, -1, -1):
    #     res[i] = postfix*res[i]
    #     postfix = postfix * nums[i]
    
    # return res

#redo 07/28/24

#pre fix gets the product of each element leading up to one before last

#postfix gets the product of each element leading up to one before first. 
# This results in a way to calculate the products befor eand after a particular index 

   
    forward = [1]*len(nums)
    reverse = [1]*len(nums)
    answer = []

    for i in range(len(nums)-1):
        forward[i+1] = forward[i] * nums[i]

    for i in range(len(nums)-1, 0, -1):
        reverse[i-1] = reverse[i] * nums[i]

    for i in range(len(forward)):
        answer.append(forward[i] * reverse[i])
    
    return answer
        