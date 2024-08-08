def isPalindrome(self, s: str) -> bool:
        
        # a more optimal solutions would be similar to two sum input array is sorted but checking if each char is the same throughout until both pointers meet in middle

        i = 0
        j = len(s)-1

        forward = ""
        reverse = ""

        while i < len(s) and j > 0:

            if s[i].isalnum():
                forward +=s[i].lower()
                i+=1
  
            else:
                i+=1
            if s[j].isalnum():
                reverse +=s[j].lower()
                j-=1
            else:
                j-=1

        temp = forward
        

        forward+=reverse[::-1]
        reverse+=temp[::-1]

        if forward == reverse:
            return True
        else:
            return False
