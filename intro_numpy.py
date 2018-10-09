import numpy as np

x = 1.0
y = 2.0

print(np.sin(x))
print(np.cos(x))
print(np.tan(x))
print(np.arcsin(x))
print(np.arccos(x))
print(np.arctan(x))
print(np.arctan2(x,y))
print(np.rad2deg(x))

print(np.sinh(x))
print(np.cosh(x))
print(np.tanh(x))
print(np.arcsinh(x))
print(np.arccosh(x))
print(np.arctanh(x))

print(np.exp(x))
print(np.log(x))
print(np.log10(x))
print(np.log2(x))

print(np.fabs(x))
print(np.fmin(x,y))
print(np.fmax(x,y))

n = 100
z = np.arange(n,dtype=float)
z *= 2.0*np.pi /float(n-1)
sin_z = np.sin (z)

print(np.interp(0.75,z,sin_z))
print(np.sin(0.75))