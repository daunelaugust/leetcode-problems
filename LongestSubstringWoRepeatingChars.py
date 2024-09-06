def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        i,j,maxLength = 0,1,1

        while j <= len(s):
            charSet = set(s[i:j])
            maxLength = max(maxLength,len(charSet))
            if len(s[i:j]) != len(charSet):
                i+=1
                charSet = set(s[i:j])
                j+=1
            else:
                j+=1
   
        return maxLength