#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

print("this script plots the hist as Fig.7ab in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")

osc_bgn=1100
osc_end=1350
theCoup=0

def load_all_sf_at_momment(c,m0,m1):
    x = array([list(load_sf_avged_over_trial(c,s,m0,m1)) \
            for s in shift_list ])
    return x

def load_odor_sf_at_momment(m0,m1):
    x = array([list(load_sf_avged_over_trial(odor_coupling,s,m0,m1)) \
            for s in shift_list ])
    return x


x=load_all_sf_at_momment(theCoup, osc_bgn, osc_end)
y=load_odor_sf_at_momment(  osc_bgn, osc_end)


tick=array(range(PN_number))
#array([0,50,100,200,300,400,500,600,700,800])
xt=x[:,tick]
xtp=PCA(xt,2)
for i in range(shift_number): plot(xtp[i,0], xtp[i,1], '.', markersize=15);
xlabel('principle component 1')
ylabel('principle component 2')
#xlim([-30,30])
#ylim([-30,30])
savefig('onnet%d_pca.jpg'%theCoup);
savefig('onnet%d_pca.eps'%theCoup);
clf()

yt=y[:,tick]
ytp=PCA(yt,2)
for i in range(shift_number): plot(ytp[i,0], ytp[i,1], '.', markersize=15);
xlabel('principal component 1')
ylabel('principal component 2')
#xlim([-30,30])
#ylim([-30,30])
savefig('offnet_pca.jpg');
savefig('offnet_pca.eps');
clf()
