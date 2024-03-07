def twoSum(self, nums: List[int], target: int) -> List[int]:
    answers = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in answers:
            return [answers[diff] , i]
        else:
            answers[nums[i]] = i  