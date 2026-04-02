def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    final_string = ''
    
    for char in s:
        if len(final_string) > 0 and final_string[-1] == char:
            final_string = final_string[:-1]
        else:
            final_string += char
            
    return final_string
        
       
      
            
       
            
       
        
       
            
   
            
        
        