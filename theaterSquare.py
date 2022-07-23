import sys
three_of_values = list(map(int, input().split(" ")))
n, m, a = 0, 0, 0
c, d = 0, 0
n = three_of_values[0]
m = three_of_values[1]
a = three_of_values[2]
if n % a == 0:
    c = n//a
else:
    c = (n//a) + 1
if m % a == 0:
    d = m//a
else:
    d = (m//a) + 1
print(str(c*d))
