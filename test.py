x = '11'
y = '111'

n1 = len(x)
n2 = len(y)

nDevide = n1//2
a = int(x[:nDevide])
b = int(x[nDevide:])
c = int(y[:(n2 - n1 + nDevide)])
d = int(y[(n2 - n1 + nDevide):])

print(a)
print(b)
print(c)
print(d)
print('nDevide: {}'.format(nDevide))
print(2//2)