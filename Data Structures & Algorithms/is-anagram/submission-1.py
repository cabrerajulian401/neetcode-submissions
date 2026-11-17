class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ''' 
         1. understand the problem 

         input: 2 str "racecar" and "carrace"

         output: bool true & false

         - Need to record the characters of each string, order is
         
         - strings have to be the same length
         - Must be the same set  

         Have 2 hash tables of the alphabet (ASCI package). For each one have a frequency of each one 

         Key of the Hashtable should be a letter, and the value should be a frequency of it. Build these first 
        ''' 

        group_1 = {}

        group_2 = {}

        for char in s: 

            if char in group_1:
                group_1[char] += 1
            else: 
                group_1[char] = 1


        for char in t:

            if char in group_2:
                group_2[char] += 1

            else:
                group_2[char] = 1


        return group_1 == group_2


                
        

        

