def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
 
        s1_map = {}
        s2_map = {}

        for i in s1:
            s1_map[i] = s1_map.get(i,0)+1

        
        
        j,k = 0, len(s1)-1

        while k < len(s2):

            if s2[j] not in s1_map or s2[k] not in s1_map:
                
                j+=1
                k+=1
                continue
            
            if s2[j] in s1_map and s2[k] in s1_map:

                k+=1
                
                
                if len(s2[j:k]) == len(s1):
                    for l in s2[j:k]:
                        s2_map[l] = s2_map.get(l,0)+1
                    print(s2_map)
                    if s2_map == s1_map:
                        print(s2_map)
                        return True
                    else:
                        j+=1
                        s2_map.clear()

                



        return False