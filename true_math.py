import math

def div_true(a, b):
  if b == 0:
    return math.inf
  else:
    return a / b

result = div_true(5, 0)
