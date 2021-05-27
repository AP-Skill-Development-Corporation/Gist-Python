def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

def even(x):
    if x%2==0:
        return x
    
def odd(n):
    if n%2!=0:
        return True
    else:
        return False
    
def perfect(number):
    #fact_sum = 0
    factors = []
    for i in range(1,number):
        if number%i==0:
            #fact_sum += i
            factors.append(i) # adding factors to the list
    #print(fact_sum)
    if sum(factors)==number:
        return True
    else:
        return False