# coding: utf-8
# follow the same approach as problem 30.
import math

digit_factorials = [ [[str(x)], math.factorial(x)] for x in range(0,10) ]

numbers = digit_factorials[1:][:]

results = []
for i in range(6):
  numbers = [ [ item[0] + digit, item[1] + factorial ] for item in numbers for digit, factorial in digit_factorials ]
  results.append(filter(lambda x: int(''.join(x[0])) == x[1] & x[1] > 1, numbers))

for item in results:
  print item
