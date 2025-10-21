class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = split(s)
        output = ""
        counter=1
        for i in reversed(words):
            output += i
            if counter+1<=len(words):
                counter+=1
                output+=" "
            
            
        return output
            

            