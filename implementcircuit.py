x=1
y=0
z=0


xANDy = x & y
yXORz= y ^ z
yORz = y | z

data = yXORz & yORz


result = xANDy ^ data


print("q = ", result)