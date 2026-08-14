class Solution:
    def isValid(self, s: str) -> bool:
        lookup = { ')': '(', ']':'[', '}':'{' }
        stack = []
        
        for char in s: #---------------------------------------------O(n)
            if char in lookup.values():
                #char opening bracket
                stack.append(char)
            else:
                #char closing bracket
                if len(stack) == 0 or stack.pop() != lookup[char]:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
            
#solution using list instead of deque