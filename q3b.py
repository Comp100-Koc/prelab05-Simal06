def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    binary_string = ''
    a_final = 0
    b_final = 0
   
    for i in range(2,len(a)):
        a_final += int(a[i]) * (2**(len(a)-1-i))
        
    for j in range(2,len(b)):
        b_final += int(b[j]) * (2**(len(b)-1-j))
         
    result = a_final + b_final
   
    if result == 0:
       return '0b0' 
   
    while result != 0:
        remainder = str(result % 2)
        binary_string += remainder
        divide = int(result / 2)
        result = divide
        
    binary_string = '0b' + binary_string[::-1]
       
       
        
    return binary_string
        
        
  
    
    
    
  
    
        
    