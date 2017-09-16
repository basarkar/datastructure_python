# Fibonacci numbers till position n.

n = input("what is the nth position? ")
n = int(n)
current = 1
next = 1
msg = "Fibonacci numbers till position " + str(n) + ": "
print(msg)
for i in range(0, n):
    print(current)
    temp_current = current
    current = next
    next += temp_current
