#---------------------------------------
# Author: Jake Stocker
# Date: 07/02/2014
# Calculates exponents value using exponentiation

# Calls function exponentiation which in turn factors the
# exponent by factoring the expression into smaller
# expresions squared
# --------------------------------------





def exponentiation(base,exponent):
    if exponent==0:
        return 1
    elif exponent==1:
        return base
    elif exponent%2==1:
        return base*exponentiation(base,exponent-1)

    else:
        temp=exponentiation(base,exponent/2)
        return temp*temp




print exponentiation(2,10)
        


