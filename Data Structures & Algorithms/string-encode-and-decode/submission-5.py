class Solution:

    def encode(self, strs: List[str]) -> str:

        payload = []

        for token in strs:
            payload.append(str(len(token)))
            payload.append('#')
            payload.append(token)
        
        return ''.join(payload)

    def decode(self, s: str) -> List[str]:

        decoded = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            str_len = int(s[i:j])
            i = j + 1
            token = s[i: i + str_len]
            i += str_len

            decoded.append(token)
        
        return decoded
