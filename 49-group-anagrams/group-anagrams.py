class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        output = []        
        for word in strs:
            sorted_string = ''.join(sorted(word))
            if sorted_string not in anagram_dict:
                output.append([])    
                anagram_dict[sorted_string] = len(output)-1
            output[anagram_dict[sorted_string]].append(word)    
        return output

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_dict = {}
#         output = []        
#         for word in strs:
#             sorted_string = ''.join(sorted(word))
#             if sorted_string not in anagram_dict:
#                 anagram_dict[sorted_string] = [word]
#             else:
#                 anagram_dict[sorted_string].append(word)
#         for key in anagram_dict:
#             output.append(anagram_dict[key])
#         return output
