#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

print("this script runs data for fig as Fig.8 in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")

tick=array([0,50,100,200,300,400,500,600,700,800])


def load_all_sf_at_momment(c,m0,m1):
    x = array([list(load_sf_avged_over_trial(c,s,m0,m1)) \
            for s in shift_list ])
    return x

def load_odor_sf_at_momment(m0,m1):
    return load_all_sf_at_momment(odor_coupling, m0, m1)


osc_bgn=1100
osc_end=1350

for theCoup in range(5):
    print(theCoup)
    x=load_all_sf_at_momment(theCoup, osc_bgn, osc_end)
    xt=x[:,tick]
    xtp=PCA(xt, len(tick), if_ret_all=True)[1] # we will only use egn-values
    savetxt('data/pca_egnval_onnet%d_osc%d_%d.txt'%(theCoup,osc_bgn,osc_end), xtp)


x=load_odor_sf_at_momment(osc_bgn, osc_end)
xt=x[:,tick]
xtp=PCA(xt, len(tick), if_ret_all=True)[1]
savetxt('data/pca_egnval_offnet_osc%d_%d.txt'%(osc_bgn,osc_end), xtp)
