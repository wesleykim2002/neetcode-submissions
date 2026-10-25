class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        print(s)
        while index < len(s):
            print(index)
            temp = index
            length = ""
            while (s[index] != "#"):
                length += s[index]
                index += 1
            length = int(length)
            # length = int(s[index])
            decoded.append(s[index+1:index+1+length])
            index += length + 1
            print(decoded)
        
        return decoded
