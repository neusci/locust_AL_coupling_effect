# !/usr/bin/env python
# -*- coding:utf-8 -*-

execfile('../../slow/slow_analy_head.py')

coupleID = 0

x=[load_sf_trial_avged(coupleID,i,50) for i in shift_list]

plot(1.0*sum(x,0)/shift_number)

savetxt("fire_rate_couple%d.txt"%(coupleID), x)

x1 = [0, 40, 80, 120, 160, 200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
xlim([0, 140])
xlabel("time (ms)")
ylabel("spike rate ($S^{-1}$)")
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
savefig("fire_rate_couple%d.jpg"%(coupleID))  # _timebin
savefig("fire_rate_couple%d.eps"%(coupleID))  # _timebin

show()
