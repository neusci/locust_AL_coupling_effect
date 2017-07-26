#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile('../slow/slow_analy_head.py')
slist=shift_list
offnet=array([load_sf_avged_over_trial(100,i,1100,1350,50) for i in slist])
onnet =array([load_sf_avged_over_trial(  0,i,1100,1350,50) for i in slist])


# this is for plot gain curve, not good
for i in range(PN_number):
    print(i)
    plot(offnet[:,i], onnet[:,i], '.');
    xlim([0,50])
    ylim([0,50])
    savefig('./fig/off2onnet_gain_curve_PN%d.jpg'%i)
    savefig('./fig/off2onnet_gain_curve_PN%d.eps'%i)
    clf()


for i in range(PN_number):
    plot(offnet[:,i], onnet[:,i], '.');

xlim([0,50])
ylim([0,50])
savefig('off2onnet_gain_curve_all.jpg')
savefig('off2onnet_gain_curve_all.eps')
savefig('./fig/off2onnet_gain_curve_all.jpg')
savefig('./fig/off2onnet_gain_curve_all.eps')
clf()
#show()
