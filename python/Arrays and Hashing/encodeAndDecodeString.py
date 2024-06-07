def encode(self, strs: List[str]) -> str:
    string = ""
    for i in strs:
        string += str(len(i))+"#"+i
    return string


def decode(self, s: str) -> List[str]:
    i = 0
    j = 0
    res = []
    while i < len(s):
        j+=1
        if s[j] == "#":
            str_len = int(s[i:j])
            i = j+1
            j = str_len + i
            string = s[i:j]
            res.append(string)

            i = j
        
    
    return res
