
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:

            count = [0] * 26 # Creating the large array for counting for each word

            for c in s:

                count[ord(c) - ord("a")] += 1  # incremetning over each letter and accessing the index 


            res[tuple(count)].append(s) # making the count list a tuple to serve as key, then appending the word to the value


        return list(res.values())  #returning res.values() as a list since it is dictionary


        

       

            