def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    # uses Neetcode bucket sort method which is bettern than my O(nlogn) solution this is O(n) time

    # result =[[] for i in range(len(nums)+1)]
    # number_map = {}
    # final_result = []

    # for i in nums:
    #     if i not in number_map:
    #         number_map[i] = 1
    #     else:
    #         number_map[i] = number_map[i]+ 1

    # for key, value in number_map.items():
    #     result[value].append(key)

    # for i in range(len(result) - 1, 0 , -1):
    #     for val in result[i]:
    #         final_result.append(val)
    #         if len(final_result) == k:
    #             return final_result

    # redo 07/28/24
    maps = {}
    for i in nums:
        maps[i] = maps.get(i, 0) + 1
    res = [[] for i in range(len(nums) + 1)]

    for t, v in maps.items():
        res[v].append(t)

    output = []

    for i in range(len(res) - 1, -1, -1):
        for j in res[i]:
            output.append(j)
            if len(output) == k:
                return output


# redo 11/25/24 took a while to get
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        resDict = {}

        freqList = [[] for i in range(len(nums) + 1)]
        res = []

        for i in nums:
            if i in resDict:
                resDict[i] += 1
            else:
                resDict[i] = 1

        for t, v in resDict.items():
            freqList[v].append(t)

        for i in range(len(freqList) - 1, 0, -1):
            for j in freqList[i]:
                res.append(j)
                if k == len(res):
                    return res
