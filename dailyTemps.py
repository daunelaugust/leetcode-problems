
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    stack = []
    i = 0
    count = 0
    res = []

    while i <= len(temperatures):
        if i == len(temperatures)-1:
            res.append(0)
            return res
        count+=1
        if not stack and temperatures[i+1] >  temperatures[i]:
            res.append(count)
            count = 0
        elif stack and temperatures[i+1] >  temperatures[i]:
            while stack[-1]<  temperatures[i]:
                stack.pop()
                count+=1
            res.append(count)
            
        i+=1
    


        

        