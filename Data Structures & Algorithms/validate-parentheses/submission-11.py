class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        combinations={ ")" : "(" , "}" : "{" , "]" : "[" }
        for i in s:
            if i in combinations:
                if stack and stack[-1] == combinations[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True 
        else:
            return False

        