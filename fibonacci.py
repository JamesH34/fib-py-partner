def fibonacci(num):
  if num <= 1:
    return num

  a = 0
  b = 1
  ph = 1
  for num in range(1, num, +1):
    ph = a + b
    a = b
    b = ph
  return ph

print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(7))

