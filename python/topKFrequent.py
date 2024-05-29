def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result =[]
        number_map = {}
        count = 1

        for i in nums:
            if i not in number_map:
                number_map[i] = 1
            else:
                number_map[i] = number_map[i]+ 1
 
        for key, value in sorted(number_map.items(), key=lambda item: item[1], reverse=True):
            if count > k:
                break
            else:
                result.append(key)
                count+=1
