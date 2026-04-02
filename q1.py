def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    empty_string = ''
    max_string = ''
    
    if len(s) > 2:
        
        
            for i in range(len(s)):   
                for j in range(i+1, len(s)):
                    active_sub = s[i : j + 1]
                    if active_sub == active_sub[::-1]:
                        if len(active_sub) >= 2 and len(active_sub) > len(max_string):
                            max_string = active_sub
            return max_string
                    
           
                        
    else:
        return empty_string
                            
        
       
                
        
                    
        
        
        
   