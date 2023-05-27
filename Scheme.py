#------------------madebyDZM-----------#

import numpy as np
import secrets
from Crypto.Util import number
from sympy import legendre_symbol
from gmpy2 import ceil, sqrt
import gensafeprime



def baby_step_giant_step(alpha, beta, p, bound=-1):
    '''
    Find x s.t. alpha^x = beta (mod p), where p is prime
    '''
    
    if(bound == -1):
        bound = p    
        
    m = int(ceil(sqrt(bound))) 
   
    T = {}
    alpha_j = 1
    for j in range(0, m):
        T[alpha_j] = j
        alpha_j = (alpha_j * alpha) % p
    
    interm = pow(alpha, -m, p)
    gamma = beta
    
    for i in range(0, m):
        if(gamma in T):
            return (i * m) + T[gamma]
        gamma = (gamma * interm) % p
    
    # No solution in {0..., bound}
    return None


def generate_safe_prime(bits, false_positive_prob=1e-24):
    while True:
        p = gensafeprime.generate(bits)
        q = (p - 1) // 2
        if(number.isPrime(p, false_positive_prob) == True and \
           number.isPrime(q, false_positive_prob) == True):
            return (p, q)



def generator_of_quadratic_residues(p):
    q = (p - 1) // 2
    while True:
        # sample g and check if g is a quadratic residue mod p
        g = secrets.randbelow(p - 1)
        legendre = legendre_symbol(g, p)
       
        if(legendre == 1): #g is a quadratic residue
            if(g != q and g % p != 1):
                return g



def is_vector_in_bound(x, B):
    max_elem = max(x)
    if(max_elem >= B):
        print("max_elem is", max_elem, ">=", B)
        return False
    
    return True



def setup(l, bits, B, false_positive_prime_prob = 1e-24):
    '''
    l    - the dimension of the vectors in Z_p*
    bits - the number of bits of the prime p
    B    - the upper bound
    
    We are working in the group of quadratic reisudes mod p
    '''

    (p, q) = generate_safe_prime(bits, false_positive_prime_prob)
    
    if((l * B * B < q) == False):
        print(q, "<= ", l * B * B, "!")
        return -100
    
    g = generator_of_quadratic_residues(p)
    
    s = []
    h = []
    
    for i in range(l):
        s.append(secrets.randbelow(q))  # s[i] is a random number from {0,1,...,q-1}
        h.append(pow(g, s[i], p))       # h[i] = ( g**(s[i]) ) % p
    
    msk = s
    mpk = (g, q, h)
    return (mpk, msk)
                


def encrypt(mpk, x, B):
	'''
	mpk = (g, q, h)
    x - vector to be encrypted
    B - upper bound
    '''
	g, q, h = mpk
	p = 2 * q + 1
	if(is_vector_in_bound(x, B) == False):
	    print("Vector x is outside the bound!")
	    return -20000

	if(len(h) != len(x)):
	    print("The dimensions of h and x are not the same!")
	    print("dim(h) =", len(h), "dim(x) =", len(x))
	    return -10000    

	r = secrets.randbelow(q)
	ct_0 = pow(g, r, p)
	Ct = [ct_0]

	for i in range(0, len(x)):
	    ct_i = ( pow(h[i], r, p) * pow(g, x[i], p) ) % p
	    Ct.append(ct_i)

	return Ct



def keygen(mpk, msk, y, B):
	g, q, h = mpk
	if(is_vector_in_bound(y, B) == False):
		print("Vector y is not in the needed bound!")
		return -10000

	if(len(msk) != len(y)):
	    print("len(msk) != len(y) !!!")
	    return -10000

	sk_y = 0
	for i in range(0, len(y)):
	    sk_y = (sk_y + (msk[i] * y[i])) % q

	return sk_y



def decrypt(mpk, Ct, sk_y, y, B):
    g, q, h = mpk
    
    p = 2*q + 1
    
    denominator_inverse = pow(Ct[0], -sk_y, p) # == ct_0 ^ (-sk_y) (mod p)
    
    product = 1
    for i in range(1, len(Ct)):
        product = (product * (pow(Ct[i], y[i-1])) % p) % p
        
    product = (product * denominator_inverse) % p 
    
    upper_bound = len(y)*B*B
    
    disc_log = baby_step_giant_step(g, product, p, upper_bound)
    
    return disc_log

