class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in  strs :
            string += str(len(word)) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            thiswordlen = int(s[i:j])
            res.append(s[j+1:j+1+thiswordlen])

            i = j+1+thiswordlen
            
        return res