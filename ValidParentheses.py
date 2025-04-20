class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []

        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                bracketStack.append(bracket)
            else:
                if len(bracketStack) == 0:
                    return False
                if bracket == ")":
                    opening = bracketStack.pop()
                    if opening != "(":
                        return False
                elif bracket == "]":
                    opening = bracketStack.pop()
                    if opening != "[":
                        return False
                elif bracket == "}":
                    opening = bracketStack.pop()
                    if opening != "{":
                        return False
            
        return len(bracketStack) == 0
