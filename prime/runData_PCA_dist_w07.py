#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

print("this script runs data for fig as Fig.6b in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")

tick=array(range(PN_number))
#array([0,50,100,200,300,400,500,600,700,800])

def load_all_sf_at_momment(c,m0,m1):
    x = array([list(load_sf_avged_over_trial(c,s,m0,m1)) \
            for s in shift_list ])
    return x

def load_odor_sf_at_momment(m0,m1):
    return load_all_sf_at_momment(odor_coupling, m0, m1)


for theCoup in range(couple_number):
    print()
    for t in range(real_begin, real_end, 50):
        print(theCoup, t)
        x=load_all_sf_at_momment(theCoup, t, t+50)
        xt=x[:,tick]
        xtp=PCA(xt,len(tick))
        savetxt('data/pca_onnet%d_time%d_%d.txt'%(theCoup,t,t+50), xtp)


for t in range(real_begin, real_end, 50):
    print(odor_coupling,t)
    x=load_odor_sf_at_momment(t, t+50)
    xt=x[:,tick]
    xtp=PCA(xt,len(tick))
    savetxt('data/pca_offnet_time%d_%d.txt'%(t,t+50), xtp)
