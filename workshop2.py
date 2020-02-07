t = (34,91,23)

type(t)

a, b, c = t

print(a,b,c)

a = {0,1,2,3,4,5}
b = {4, 5, 6, 7, 8, 9}

type(a)

a & b

a | b

d = {
     'name': 'John',
     'height': 1.84,
     'age': 34,
     'mobile': ['862-912-44','01619202529'],
     'address': {
         'country': 'US',
         'state': 'NY',
         'street': '55 and main',
         'house':{
             'road': 'Error 404'
         }
     }
}
d['name']
d['address']['country']
d.keys()
d['address'].keys()
d['address']['house'].keys()
for key,value in d.items():
  print(f'{key}:{value}')

a=['John','Smith','Sto']
#numpy

import numpy as np
a = np.array(a)
a
b=np.array([2,3,5,7,11,13,17,19])
type(b)
b.shape
#b.reshape((2,2))
#broadcast
a = np.array([[0,1,2],
              [-1,3,0],
              [-2,4,1]])
a
a[0:2,1]
a[0:2,1:3]
a[0:2:]
a ** 2
a.dot(a)
x = np.array([[2,3],[1,9]])
y = np.array([[0,-2],[-1,3]])
x*y
x.dot(y) #matrix multiplication
b = np.array([[0,1,2],
              [-1,3,0],
              [-2,4,1]])
b[1:]=b[1:]**2
b[1:]
b
p1 = np.poly1d([1,9,-4,-16,5])
print(p1)

p1.roots

x = np.linspace(-10,2.5,100) #(from,to,howManyPoints)
x
y = p1(x)
y

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.hlines(y=0,xmin=-2.5,xmax=2.5)

p2 = np.poly1d([1,2,1])
print(p2)
p3 = p1 * p2
p3.roots

a

b

b
b_i = np.linalg.inv(b) #inverse
b_i
b.dot(b_i)
b_i = np.linalg.pinv(b) #sudo inverse

