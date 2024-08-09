def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #correct

        stack = []
        array = [0]*len(temperatures)

        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                res = stack.pop()
                array[res[1]] = i - res[1]
     
            stack.append([temperatures[i], i])
           
        return array


        #redo 08/03/24
    #    stack = []
    #     res = [0]*len(temperatures)

    #     for i in range(len(temperatures)):
    #         while stack and stack[-1][0] < temperatures[i]:
    #             temp, ind = stack.pop()
    #             res[ind]= i - ind

    #         stack.append([temperatures[i],i])

    #     return res
        