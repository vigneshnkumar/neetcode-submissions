class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {"{":"}", "(":")", "[":"]"}
        current = []

        for char in s:

            if char in brackets:
                current.append(char)
            
            if char in brackets.values():

                if len(current) == 0:
                    return False

                if brackets[current[-1]] == char:
                    current.pop()
                    continue
                elif brackets[current[-1]] == char:
                    current.pop()
                    continue
                elif brackets[current[-1]] == char:
                    current.pop()
                    continue
                else:
                    return False
        return (len(current)) == 0



        