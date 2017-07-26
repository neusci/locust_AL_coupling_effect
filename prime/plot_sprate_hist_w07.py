#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile("../slow/slow_analy_head.py")

print("this script plots the hist as Fig.6b in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")

osc_bgn=1100
osc_end=1350


def load_all_sf_at_momment(m0,m1):
    x = array([list(load_sf_avged_over_trial(c,s,m0,m1)) \
            for c in range(couple_number) \
            for s in shift_list ])
    return array(x.flat)

def load_odor_sf_at_momment(m0,m1):
    x = array([list(load_sf_avged_over_trial(odor_coupling,s,m0,m1)) \
            for s in shift_list ])
    return array(x.flat)


x=load_all_sf_at_momment( osc_bgn, osc_end)
y=load_odor_sf_at_momment(osc_bgn, osc_end)


hist(x, 20, normed=1, histtype='bar', color='b', alpha=0.75);
xlabel('firing rate (Hz)')
ylabel('fraction')
savefig('hist-onNet-osc.jpg')
savefig('hist-onNet-osc.eps')
clf()

hist(y, 20, normed=1, histtype='bar', color='b', alpha=0.75);
xlabel('firing rate (Hz)')
ylabel('fraction')
savefig('hist-offNet-osc.jpg')
savefig('hist-offNet-osc.eps')
clf()
