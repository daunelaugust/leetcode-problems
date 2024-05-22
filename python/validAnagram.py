def isAnagram(self, s: str, t: str) -> bool:

    # Make a map to store the freq of each char
    str1 ={}

    #Loop thru first string
    for i in s:
        #updates freqs of exisiting char
        if i in str1:
            str1[i] = str1[i] + 1
        # inits a new char to 1
        else:
            str1[i] = 1

    #repeat for second string
    str2 ={}
    for i in t:
        if i in str2:
            str2[i] = str2[i] + 1
        else:
            str2[i] = 1

    # compares both string contents, using 'is' compares if its the same object instead
    return str1 == str2