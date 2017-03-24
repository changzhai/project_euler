# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

instructions = """
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import utils

def is_abundant(n):
    if sum(utils.factors(n)) - n > n:
        return True
    else: 
        return False
    
abundant = []
total = 0
for x in range(1,28123+1):
    not_abundant = True
    if is_abundant(x):
        abundant.append(x)
        print(str(x) + ' is abundant')
    
    for n in [n for n in abundant if x/n>=2]:
        if (x - n) in abundant:
            not_abundant = False
            break
    if not_abundant:
        total += x
        print(str(x) + ', total = ' + str(total))
    else:
        print(str(x) + 'is the sum of abundants')
print(total)