class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            if num not in my_map:
                my_map[num] = 1
                continue
            my_map[num] += 1
        
        sorted_dict_desc = dict(sorted(my_map.items(), key=lambda item: item[1], reverse=True))

        result = []
        current = 0

        for key, value in sorted_dict_desc.items():
            if current > k - 1:
                break
            result.append(key)
            current += 1
        
        return result