# coding: utf-8

digit_powers = [ [[str(x)], x**5] for x in range(0,10) ]
numbers = digit_powers[:]

for i in range(6):
  numbers = [ [ item[0] + digit, item[1] + power ] for item in numbers for digit, power in digit_powers ]
  results = filter(lambda x: int(''.join(x[0])) == x[1] & x[1] > 1, numbers)

for item in results:
  print item
