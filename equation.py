from pip._vendor.distlib.compat import raw_input


def coordinate(a, b, c, d, e, f):
    y = (f - c * (d / a)) / (e - b * (d / a))
    x = (c - (b * y)) / a

    print(f'{x} {y}')


# main
print("Find coordinates of x and y")
print("Equation is ax+by+c=0 and dx+ey+f=0")
a, b, c, d, e, f = map(float, raw_input("Enter a,b,c,d,e,f\n").split())
print("Intersecting points are given")
coordinate(a, b, c, d, e, f)
