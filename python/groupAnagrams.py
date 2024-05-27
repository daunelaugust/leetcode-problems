def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #Initialize a map

    word_map = {}

    # for each word sort it and store as a key for dict
    for i in strs:
        word = sorted(i)
        word = ''.join(word)
        # for the current word store as a value for the stored anagram 
        # The sorted key will be the same for all anagrams
        if word not in word_map:
            word_map[word] = []
        word_map[word].append(i)


    return word_map.values()

