
def __init__(self):
    self.map = defaultdict(list)
    

def set(self, key: str, value: str, timestamp: int) -> None:
    self.map[key].append([value,timestamp])
    

def get(self, key: str, timestamp: int) -> str:
    array = self.map[key]

    if not array:
        return ""
    
    l = 0
    r=len(array)-1
    
    #make true if solution found,. false if not found then decrement array
    flag = False
    

    while l<=r:
        mid = (l+r)//2

        

        if array[mid][1] == timestamp:
            flag = True
            break
        elif timestamp > array[mid][1]:
            l = mid +1
        else:
            r = mid - 1 
    
    if flag:
        return array[mid][0]
    else:
        while mid>-1:
            if array[mid][1] > timestamp:
                mid = mid -1
            elif array[mid][1] < timestamp:
                return array[mid][0]
        return ""