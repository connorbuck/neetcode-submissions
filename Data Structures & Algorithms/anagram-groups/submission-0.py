class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in my_map:
                my_map[sorted_word] = [word]
                continue
            my_map[sorted_word].append(word)
        
        result = []
        for key, value in my_map.items():
            result.append(value)
        return result