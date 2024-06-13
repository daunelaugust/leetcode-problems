def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    stack = []
    array = [0]*len(temperatures)

    for i in range(len(temperatures)):
        
        if i == len(temperatures)-1:
            break

        print(stack)
        while stack and stack[-1][0] < temperatures[i]:
            res = stack.pop()
            array[res[1]] = i - res[1]
    


        stack.append([temperatures[i], i])
        
    return array


        

        