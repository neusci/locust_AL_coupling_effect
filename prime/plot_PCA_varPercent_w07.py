#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

print("this script plots fig as Fig.8 in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")

tick=array([0,50,100,200,300,400,500,600,700,800])

osc_bgn=1100
osc_end=1350

x0=loadtxt('data/pca_egnval_onnet0_osc%d_%d.txt'%(osc_bgn,osc_end))
x1=loadtxt('data/pca_egnval_onnet1_osc%d_%d.txt'%(osc_bgn,osc_end))
x2=loadtxt('data/pca_egnval_onnet2_osc%d_%d.txt'%(osc_bgn,osc_end))
x3=loadtxt('data/pca_egnval_onnet3_osc%d_%d.txt'%(osc_bgn,osc_end))
x4=loadtxt('data/pca_egnval_onnet4_osc%d_%d.txt'%(osc_bgn,osc_end))

z=loadtxt('data/pca_egnval_offnet_osc%d_%d.txt'%(osc_bgn,osc_end))

# change to percents
x0 /= sum(x0)
x1 /= sum(x1)
x2 /= sum(x2)
x3 /= sum(x3)
x4 /= sum(x4)
z /= sum(z)

x=(x0+x1+x2+x3+x4)/5.0

plot(x, 'o-', markersize=15, label='on network')
plot(z, '*-', markersize=15, label='off network')

#plot(x0)
#plot(x1)
#plot(x2)
#plot(x3)
#plot(x4)

legend()
xlabel('principal component')
ylabel('percentage of variance')
savefig('egnval-dist.jpg')
clf()
