    def minWindow(self, s: str, t: str) -> str:

        #Follows neetcode solution

        if len(s)<len(t):
            return ""

        c1 = Counter(t)
        c2  = {}
        need = len(c1)
        have = 0
        l = 0
        res = ""
        minLen = float("inf")



        for r in range(len(s)):
            char = s[r]


            c2[char] = c2.get(char,0)+1

            

            if char in c1 and c2[char] == c1[char]:
                have+=1

            while have == need:
                if(r-l+1)<minLen:
                    res = s[l:r+1]
                    minLen = (r-l+1)
                c2[s[l]]-=1
                if s[l] in c1 and c2[s[l]] < c1[s[l]]:
                    have-=1
                l+=1

        if minLen != float("inf"):
            return res
        else:
            return ""