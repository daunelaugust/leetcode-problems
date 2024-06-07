def longestConsecutive(self, nums: List[int]) -> int:
    number_set= set(nums)

    max_count = 0

    for n in nums:
        #check if the current number is a start of a possible sequence
        if (n-1) not in number_set:
            count = 0
            while(n+count) in number_set:
                count+=1
                if count > max_count:
                    max_count =count
    return max_count
        
            



