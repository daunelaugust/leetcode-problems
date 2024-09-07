def maxProfit(self, prices: List[int]) -> int:

    k = 1
    i = 0

    maxProf = 0

    while k < len(prices):
        maxProf = max(prices[k]-prices[i],maxProf)
        if prices[i] > prices[k]:
            i=k
            k+=1
            
        else:
            k+=1
    
    return maxProf