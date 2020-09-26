import cmath
x=list(map(complex,input().split()))
a=x[0]
print(abs(complex(a.real,a.imag)))
print(cmath.phase(complex(a.real, a.imag)))