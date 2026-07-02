class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary (hash map) to map each closing bracket to its opening partner
        # This allows us to check if 'char' is a closing bracket in O(1) time
        brackets = {"}":"{", ")":"(", "]":"["}
        
        # Initialize an empty list 'current' to act as our Stack (LIFO: Last-In, First-Out)
        current = []

        # Loop through every character in the input string 's'
        for char in s:

            if char in brackets.values(): 
                # If the character is a opening bracket, it's an opening bracket
                # We "push" it onto our stack to be matched later
                current.append(char)

            # Check if the current character is a closing bracket?
            elif char in brackets: 
                
                # We need to verify two things before closing:
                # 1. 'current': Is the stack NOT empty? (A closing bracket needs an opener before it)
                # 2. 'current[-1] == brackets[char]': Does the most recently opened bracket match this closer?
                if current and current[-1] == brackets[char]:
                    # If it matches, remove the successfully paired opening bracket from the top of the stack
                    current.pop()
                else:
                    # If the stack was empty OR the top didn't match the correct opener, it's invalid
                    return False
            


        # After the loop, the string is valid ONLY if every opening bracket was closed
        # 'not current' returns True if the list is empty, and False otherwise
        return True if not current else False