class Solution:
    def isValid(self, s: str) -> bool:
        
        openers = ["{","(","["]
        closers = ["}",")","]"]
        current = []

        for char in s:

            if char in openers:
                current.append(char)
            
            elif char in closers:

                if len(current) == 0:
                    return False

                elif char == "}" and current[-1] == "{":
                    current.pop()
                    continue
                elif char == ")" and current[-1] == "(":
                    current.pop()
                    continue
                elif char == "]" and current[-1] == "[":
                    current.pop()
                    continue
                else:
                    return False
        return (len(current) == 0)



        