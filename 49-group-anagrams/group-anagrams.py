class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        output = []        
        for word in strs:
            sorted_string = ''.join(sorted(word))
            if sorted_string not in anagram_dict:
                output.append([])    
                anagram_dict[sorted_string] = len(output)-1
            print(anagram_dict[sorted_string])
            output[anagram_dict[sorted_string]].append(word)    
                # anagram_dict[sorted_string].append(word)
        # for key in anagram_dict:
        #     output.append(anagram_dict[key])
        return output
