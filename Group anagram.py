def group_anagrams(strs):
    anagram_map = {}
    
    for word in strs:
        sorted_word = tuple(sorted(word))
        
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
            
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_list))
