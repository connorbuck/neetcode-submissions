class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_map = {}
        t_char_map = {}

        for c in s:
            if c not in s_char_map:
                s_char_map[c] = 1
                continue
            s_char_map[c] += 1
        
        for c in t:
            if c not in t_char_map:
                t_char_map[c] = 1
                continue
            t_char_map[c] += 1
        
        if len(s_char_map) != len(t_char_map):
            return False
        
        for key, value in s_char_map.items():
            if key not in t_char_map:
                return False
            
            if value != t_char_map[key]:
                return False
        
        return True