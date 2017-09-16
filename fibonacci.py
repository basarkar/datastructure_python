# Fibonacci numbers till position n.

n = 12
current = 1
next = 1
msg = "Fibonacci numbers till position " + repr(n) + ": "
print(msg)
for i in range(1, n):
    print(current)
    temp_current = current
    current = next
    next += temp_current
