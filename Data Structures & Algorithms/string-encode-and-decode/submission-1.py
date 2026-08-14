class Solution:

#customized delimeter 


    def encode(self, strs: List[str]) -> str:
        delimeter = "**..*."
        s = ''
        for i in range(len(strs)):
            s += strs[i] + delimeter # check syntax
        return s

    def decode(self, s: str) -> List[str]:
        delimeter = s[len(s)-6:len(s)] # returns delimeter
        res = []

        index = 0 
        elm = ''

        while index < len(s):
            if s[index] != delimeter[0]:
                elm += s[index]
                index += 1
            else:
                #checking potential delimeter
                temp = s[index:index+6]
                if temp == delimeter: #found our element
                    res.append(elm)
                    elm = ''
                    index = index + 6 #jumps to character after delimeter
                else:
                    elm += s[index]
                    index += 1
        
        return res