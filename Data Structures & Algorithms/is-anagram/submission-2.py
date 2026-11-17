class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ''' 

        input: 2 str as vars s and t 
        output: bool (True,False)

        example: 

        Input: s = "racecar" t = "carrace" 

        logic: Each as 2 A's, 2 R's, 2 C's, and 1 E for a total of 7 characters 

        Order is neglible. Note: 2 dic's are equal to eachother regardless of order
        For 2 dicts of each one and see if they are equal 

        map = {character: frequency}


        1. build each map of lists
            - If not in list then create the new value and set it to 1
            - If already in list then increment by 1 

    ''' 

        s_chars = {}

        t_chars = {} 


        for char in s: 

            if char in s_chars: 
                s_chars[char] += 1 

            else: 

                s_chars[char] = 1

        print(s_chars)


        for char in t: 

            if char in t_chars: # if char checks the keys
                t_chars[char] += 1 

            else: 

                t_chars[char] = 1

        print(t_chars)

        if t_chars == s_chars:
            return True 

        else: return False

        






        

                
        

        

