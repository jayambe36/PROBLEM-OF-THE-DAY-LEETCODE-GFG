class Solution(object):
    def lengthOfLongestSubstring(self, s):
      
        lst_seen = {} # mapping from character to its last seen index in s
        strt = 0 # start index of current substring 
        longest = 0
        
        for i, c in enumerate(s):
            
            if c in lst_seen and lst_seen[c] >= strt:
                # start a new substring after the previous of c
                strt = lst_seen[c] + 1
            else : 
                longest = max(longest, i - strt + 1)
            
            lst_seen[c] = i # update the last sighting index
                
        return longest
        
#Maintain a sliding window, updating the start wheneverwe see a character repeated.
## Time complexity : O(n)
## Space complexity : O(1), dictionary is limited by a fixed size alphabet
