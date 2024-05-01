def factores(x): # return a list with prime factors of x
    
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

def is_prime(x): # return if the input is a prime number
	
    if x < 2 or (x % 2 == 0) and x != 2: 
        return False
		
    for i in range(2, (x // 2) + 1): 
        
    	if x % i == 0: 
    		return False

    return True

def lcm(x,y): # return the least common multiple
    
    bigger = max(x,y)
        
    while True:
        
        if bigger % x == 0 and bigger % y == 0:
            return(bigger)
            break
        
        bigger += 1

def gdc(x,y): # return the greatest common divisor
    
    if y == 0:
        return x
    else:
        return mdc(y, (x % y))