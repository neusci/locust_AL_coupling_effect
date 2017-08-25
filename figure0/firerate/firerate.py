# !/usr/bin/env python
# -*- coding:utf-8 -*-

execfile('../../slow/slow_analy_head.py')

coupleID = 0
x=[load_sf_trial_avged(coupleID,i,50) for i in shift_list]
savetxt("fire_rate_couple%d.txt"%(coupleID), x)

plot(1.0*sum(x,0)/shift_number)
xticks([0, 40, 80, 120, 160, 200], ['0', '2000', '4000', '6000', '8000', '10000'])  #, rotation='vertical')
xlim([0, 140])
xlabel("time (ms)")
ylabel("spike rate (Hz)")
axvspan(22, 27, facecolor='0.75', alpha=0.75) # 21-27:50-350ms => 100-400ms
axhline(y=-0.1, xmin=0.15, xmax=0.54, lw=2, color='gray')

savefig("fire_rate_couple%d.jpg"%(coupleID))  # _timebin
savefig("fire_rate_couple%d.eps"%(coupleID))  # _timebin
show()
