class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        encoded = []

        for payload in strs:
            encoded.append(str(len(payload)))
            encoded.append(delimiter)
            encoded.append(payload)
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        # chars = list(s)
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
                print(j)
            
            payload_len = int(s[i:j])
            payload = s[j+1 : j+1+payload_len]
            decoded.append(payload)

            i = j + 1 + payload_len

        return decoded