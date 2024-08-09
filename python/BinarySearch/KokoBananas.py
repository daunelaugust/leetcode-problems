def minEatingSpeed(self, piles: List[int], h: int) -> int:
    minPile = 1
    maxPile = 1
    for i in piles:
        minPile = min(i,minPile)
        maxPile = max(i,maxPile)

    while minPile <= maxPile:
        mid = (minPile+maxPile)//2
        sumPiles = 0

        for i in piles:

            sumPiles += math.ceil(i/mid)
        
        if sumPiles > h:
            minPile = mid+1
            
        else:
            maxPile = mid -1
            
    return minPile