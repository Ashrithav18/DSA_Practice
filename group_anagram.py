def groupAnagrams(strs):
    anagram_map = {}

    for word in strs:
        # Sort the word to use as key
        key = ''.join(sorted(word))

        # Add to dictionary
        if key not in anagram_map:
            anagram_map[key] = []

        anagram_map[key].append(word)

    # Return grouped anagrams
    return list(anagram_map.values())


# ----------- MAIN PROGRAM -----------

strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

print(groupAnagrams(strs1))
print(groupAnagrams(strs2))
print(groupAnagrams(strs3))