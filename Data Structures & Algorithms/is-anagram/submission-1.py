class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_holder = {}
        t_holder = {}

        for pointer in s:
          
            if pointer not in s_holder:
                s_holder[pointer] = 1
            else:
                s_holder[pointer] += 1

        for pointer in t:
           
            if pointer not in t_holder:
                t_holder[pointer] = 1
            else:
                t_holder[pointer] += 1


        if s_holder == t_holder:
            return True
        
        return False
            



        