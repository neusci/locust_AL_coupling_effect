#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

print("please run run_bandpower.py to generate the bandpower_c_s.txt")
print("BEFORE run plot_bandpower.py to generate figures")
execfile("../../slow/slow_analy_head.py")

#couple_number=5 # use 5 couples only?
bp_list = [loadtxt("data/bandpower_50ms_%d_%d.txt"%(coupleID,shiftID))
           for coupleID in ptCouple_list
           for shiftID  in ptShift_list]

bp_avg = 1.0*sum(bp_list,0)/(ptCouple_number*ptShift_number)

figure()
plot(bp_avg)
xlabel("time (ms)")
ylabel("bandpower")
xticks([0,20,40,60,80, 100,120,140], ['0','1000','2000','3000','4000', '5000','6000','7000'])  #, rotation='vertical')
axvspan(22, 27, facecolor='0.75', alpha=0.75) # 21-27:50-350ms => 100-400ms
axhline(y=0.0, xmin=0.15, xmax=0.54, lw=1, color='gray')
savefig("bandpower_avg_over_%dc_%ds_paraTest.jpg"%(ptCouple_number,ptShift_number))
savefig("bandpower_avg_over_%dc_%ds_paraTest.eps"%(ptCouple_number,ptShift_number))
clf()
