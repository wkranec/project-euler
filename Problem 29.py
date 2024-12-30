values = {}

for a in xrange(2,101):
  for b in xrange(2, 101):
    power = a**b
    if values.has_key(power):
      values[power] += 1
    else:
      values[power] = 1

print len(values.keys())
