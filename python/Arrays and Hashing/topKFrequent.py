def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    #uses Neetcode bucket sort method which is bettern than my O(nlogn) solution this is O(n) time

    result =[[] for i in range(len(nums)+1)]
    number_map = {}
    final_result = []

    for i in nums:
        if i not in number_map:
            number_map[i] = 1
        else:
            number_map[i] = number_map[i]+ 1

    for key, value in number_map.items():
        result[value].append(key)

    for i in range(len(result) - 1, 0 , -1):
        for val in result[i]:
            final_result.append(val) 
            if len(final_result) == k:
                return final_result
    