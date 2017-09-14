#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile("../slow/slow_analy_head.py")

print("this script plots the hist as Fig.6b in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")
print("taken from locust_AL_aa/prime, revised")
print()


osc_bgn=1100
osc_end=1350
#sList=[0]
sList = ptShift_list


def load_resp_sf_at_momment(cc,m0,m1):
    x = array([list(load_sf_avged_over_trial(cc,s,m0,m1)) for s in sList])
    return array(x.flat)


def load_odor_sf_at_momment(m0,m1):
    x = array([list(load_sf_avged_over_trial(odor_coupling,s,m0,m1)) for s in sList])
    return array(x.flat)


y=load_odor_sf_at_momment(osc_bgn, osc_end)
if len(sList)==1:
    savetxt('./data/hist_offNet_s%d_paraTest.txt'%sList[0], y)
else:
    savetxt('./data/hist_offNet_paraTest.txt', y)
#...
hist(y, 20, normed=1, histtype='bar', color='green', alpha=0.75);
xlabel('firing rate (Hz)')
ylabel('fraction')
if len(sList)==1:
    savefig('hist_offNet_osc_c%d_s%d_paraTest.jpg'%(odor_coupling,sList[0]))
    savefig('hist_offNet_osc_c%d_s%d_paraTest.eps'%(odor_coupling,sList[0]))
else:
    savefig('hist_offNet_osc_c%d_paraTest.jpg'%odor_coupling)
    savefig('hist_offNet_osc_c%d_paraTest.eps'%odor_coupling)
clf()


for c in ptCouple_list:
    x=load_resp_sf_at_momment(c, osc_bgn, osc_end)
    if len(sList)==1:
        savetxt('./data/hist_onNet_c%d_s%d_paraTest.txt'%(c,sList[0]), x)
    else:
        savetxt('./data/hist_onNet_c%d_paraTest.txt'%c, x)
    #...
    hist(x, 20, normed=1, histtype='bar', color='purple', alpha=0.75);
    xlabel('firing rate (Hz)')
    ylabel('fraction')
    if len(sList)==1:
        savefig('hist_onNet_osc_c%d_s%d_paraTest.jpg'%(c,sList[0]))
        savefig('hist_onNet_osc_c%d_s%d_paraTest.eps'%(c,sList[0]))
    else:
        savefig('hist_onNet_osc_c%d_paraTest.jpg'%c)
        savefig('hist_onNet_osc_c%d_paraTest.eps'%c)
    clf()
