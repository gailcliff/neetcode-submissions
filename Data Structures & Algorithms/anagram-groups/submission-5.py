class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list[str])

        for stri in strs:
            vector = [0] * 26

            for ch in stri:
                vector[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(vector)].append(stri)
        
        return list(anagrams.values())