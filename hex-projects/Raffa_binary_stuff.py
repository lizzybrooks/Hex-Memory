# Raphael Gonzalez binary to decimal conversion algorithm

def is_1(num): # takes in individual 1s or 0s
    if num == 1:
        return True
    elif num == 0:
        return False
    else:
        exit('numbers are not binary')

def to_dec(nums): # takes in string of 1s and 0s and returns the decimal value, has no limit to string length
    dec = 0
    print(len(nums))
    for i, s in enumerate(nums):
        n = int(s)
        pwr = (len(nums)-1)-i
        if is_1(n):
            p = 2**pwr
            dec = dec + p
    return dec

# print( to_dec("0011101000101001") )

def get_pwr(n, p, b):
    pwr = p
    if n == 1:
      return pwr
    elif n % b > 0:
        n = n - 1
        return get_pwr(n, pwr, b)
    else:
        return get_pwr(n/b, pwr+1, b)

def to_bi(n):
    bi_str = ''
    pwr = get_pwr(n, 0, 2)
    num = n

    for i in xrange(pwr+1):
        pw = pwr - i
        if num >= 2**pw:
            bi_str = bi_str + '1'
            num = num - 2**pw
        else:
            bi_str = bi_str + '0'
    a_n = len(bi_str)
    if a_n < 8:
        bi_str = '0'*(8-a_n)+bi_str
    return bi_str

# print(to_bi(36))
from random import *

def rand_img(d): # this is a random img generator input d is the the dimensions of a square
    c_str = ''
    for i in xrange(d**2):
        for j in xrange(3):
            num = randint(0, 255)
            byte = to_bi(num)
            c_str= c_str + byte
    return c_str