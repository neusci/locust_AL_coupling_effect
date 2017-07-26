#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile("../slow/slow_analy_head.py")

print("this script plots the hist as Fig.6b in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")
print("taken from locust_AL_aa/prime, revised")
print()


osc_bgn=1100
osc_end=1350
c = 0
#sList=[0]
sList=shift_list


def load_resp_sf_at_momment(m0,m1):
    x = array([list(load_sf_avged_over_trial(c,s,m0,m1))
            for s in sList])
    return array(x.flat)


def load_odor_sf_at_momment(m0,m1):
    x = array([list(load_sf_avged_over_trial(odor_coupling,s,m0,m1))
            for s in sList])
    return array(x.flat)


x=load_resp_sf_at_momment(osc_bgn, osc_end)
y=load_odor_sf_at_momment(osc_bgn, osc_end)
if len(sList)==1:
    savetxt('./data/hist_onNet_s%d.txt'%sList[0], x)
    savetxt('./data/hist_offNet_s%d.txt'%sList[0], y)
else:
    savetxt('./data/hist_onNet.txt', x)
    savetxt('./data/hist_offNet.txt', y)


hist(x, 20, normed=1, histtype='bar', color='b', alpha=0.75);
xlabel('firing rate (Hz)')
ylabel('fraction')
if len(sList)==1:
    savefig('hist_onNet_osc_s%d.jpg'%sList[0])
    savefig('hist_onNet_osc_s%d.eps'%sList[0])
else:
    savefig('hist_onNet_osc.jpg')
    savefig('hist_onNet_osc.eps')
clf()


hist(y, 20, normed=1, histtype='bar', color='b', alpha=0.75);
xlabel('firing rate (Hz)')
ylabel('fraction')
if len(sList)==1:
    savefig('hist_offNet_osc_s%d.jpg'%sList[0])
    savefig('hist_offNet_osc_s%d.eps'%sList[0])
else:
    savefig('hist_offNet_osc.jpg')
    savefig('hist_offNet_osc.eps')
clf()


# --- plot new periods:


prd_bgn2=2000
prd_end2=3500

z=load_resp_sf_at_momment(prd_bgn2, prd_end2)
if len(sList)==1:
    savetxt('./data/hist_onNet_period2_s%d.txt'%sList[0], z)
else:
    savetxt('./data/hist_onNet_period2.txt', z)

hist(z, 20, normed=1, histtype='bar', color='b', alpha=0.75);
xlabel('firing rate (Hz)')
ylabel('fraction')
if len(sList)==1:
    savefig('hist_onNet_period2_s%d.jpg'%sList[0])
    savefig('hist_onNet_period2_s%d.eps'%sList[0])
else:
    savefig('hist_onNet_period2.jpg')
    savefig('hist_onNet_period2.eps')
clf()


prd_bgn3=3500
prd_end3=4500

zz=load_resp_sf_at_momment(prd_bgn3, prd_end3)
if len(sList)==1:
    savetxt('./data/hist_onNet_period3_s%d.txt'%sList[0], zz)
else:
    savetxt('./data/hist_onNet_period3.txt', zz)

hist(zz, 20, normed=1, histtype='bar', color='b', alpha=0.75);
xlabel('firing rate (Hz)')
ylabel('fraction')
if len(sList)==1:
    savefig('hist_onNet_period3_s%d.jpg'%sList[0])
    savefig('hist_onNet_period3_s%d.eps'%sList[0])
else:
    savefig('hist_onNet_period3.jpg')
    savefig('hist_onNet_period3.eps')
clf()
