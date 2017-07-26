#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

print("please run run_bandpower.py to generate the bandpower_c_s.txt")
print("BEFORE run plot_bandpower.py to generate figures")
execfile("../slow/slow_analy_head.py")

#couple_number=5 # use 5 couples only?
bp_list = [loadtxt("data/bandpower_50ms_%d_%d.txt"%(coupleID,shiftID)) \
    for coupleID in range(couple_number) for shiftID  in shift_list]

bp_avg = 1.0*sum(bp_list,0)/(couple_number*shift_number)

figure()
plot(bp_avg)
xlabel("time (ms)")
ylabel("bandpower")
x1 = [0, 20, 40,60, 80, 100,120, 140]
labels1 = ['0', '1000','2000','300', '4000', '5000','6000', '7000']
xticks(x1, labels1)  #, rotation='vertical')
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
savefig("bandpower_avg_over_%dc_%ds.jpg"%(couple_number,shift_number))
savefig("bandpower_avg_over_%dc_%ds.eps"%(couple_number,shift_number))
clf()
