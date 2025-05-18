class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_dict = {}
        for char in s:
            if char not in string_dict:
                string_dict[char] = 1
            else:
                string_dict[char] += 1

        for char in t:
            if char not in string_dict:
                return False
            else:
                string_dict[char] -= 1
                if string_dict[char] == 0:
                    del string_dict[char]
        
        if len(string_dict) == 0:
            return True
        else:
            return False