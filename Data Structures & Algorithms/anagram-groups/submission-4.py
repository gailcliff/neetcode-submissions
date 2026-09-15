class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            vector = [0] * 26

            for ch in s:
                vector[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(vector)].append(s)
        
        return list(anagrams.values())