# !/usr/bin/env python
# -*- coding:utf-8 -*-

execfile('../../slow/slow_analy_head.py')

coupleID = 0
x = zeros( int(round((real_end-real_begin)/50)) ) # 50 is cd

for shiftID in shift_list:
    x += loadtxt("./data/response_couple%d_shift%d.txt"%(coupleID,shiftID))

x /= shift_number

figure()
plot(x)
ylabel("response PN rate (%)")
x1 = [0, 40, 80, 120, 160, 200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
xlim([0, 140])
axvspan(22, 27, facecolor='0.75', alpha=0.75) # 21-27:50-350ms => 100-400ms
axhline(y=-0.1, xmin=0.15, xmax=0.54, lw=4, color='gray')
xlabel("time (ms)")
savefig("response_couple%d.jpg"%(coupleID))
savefig("response_couple%d.eps"%(coupleID))
clf()
