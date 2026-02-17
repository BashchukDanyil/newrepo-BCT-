import utils.py as utils
print(utils.factorial(5))

def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a) 
