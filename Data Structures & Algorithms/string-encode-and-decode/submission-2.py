class Solution:

    def encode(self, strs: List[str]) -> str:
        #First character in encoded is always len of the first word, len+1 is
        #length of second word and so on
        ## [] is handled as an empty string, [""] encodes as a 0


        #got stuck on what to do if word is more than one digit,
        #pair with a delimiter and read up to it to find len
        encoded = ""

        if len(strs) == 0:
            return encoded
        else:
            for word in strs:
                encoded += str(len(word)) + "#" + word
        return(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        if s == "":
            return decoded
        else:
            i = 0
            while i<len(s)-1:
                length = 0
                temp = ""
                while s[i] != "#":
                    temp += s[i]
                    i += 1
                length = int(temp)

                if length == 0:
                    decoded.append("")
                    i+=1
                else:
                    thisword = ""
                    for j in range(length):
                        thisword += s[i+1]
                        i+=1
                    decoded.append(thisword)
                    i += 1
            return decoded
    
        
