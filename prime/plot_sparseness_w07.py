#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

print("this script plots the life-sparseness Fig.3b in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")


def sparseness(ls):
    ls2 = ls**2
    return (1.0-avg(ls)**2/avg(ls2))/(1-1.0/len(ls))


def sparse_at_momment(c,s,m0,m1):
    x = array([list(load_sf_from_file(c,s,i,m0,m1)) \
               for i in range(trial_number)])
    return array([sparseness(x[:,j]) for j in range(PN_number)])


x=sparse_at_momment(0,0,1100,1350)
y=sparse_at_momment(0,0,1500,4000)

print(x)
print(y)
plot(x,y,'.')
savefig('sp.jpg')
clf()
