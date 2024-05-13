#
# return if x is a prime number
#

def is_prime(x): 
	
    if x < 2 or ((x % 2 == 0) and x != 2): 
        return False
		
    for i in range(2, (x // 2) + 1): 
        
    	if x % i == 0: 
    		return False

    return True
	
# 
# return a list with prime factors of x
#

def factors(x): 
    
    prime_fact = []
    while x % 2 == 0:
        prime_fact.append(2),
        x /= 2
        
    for i in range(3,int(x),2):
          
        while x % i== 0:
            prime_fact.append(int(i))
            x /= i
            
    if x > 2:
        prime_fact.append(int(x))
        
    return prime_fact 

#
# return the least common multiple
#

def lcm(x,y): 
    
    c_mult = max(x,y)
        
    while True:
        
        if c_mult % x == 0 and c_mult % y == 0:
            return(c_mult)
            break
        
        c_mult += 1

#
# return the greatest common divisor
#

def gdc(x,y): 
    
    if y == 0:
        return x
    else:
        return gdc(y, (x % y))
