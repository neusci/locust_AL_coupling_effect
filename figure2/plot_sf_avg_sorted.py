#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

tbgn=1100
tend=1350

cList=[100] #[0] # range(couple_number)
cNum=len(cList)  # couple_number

print('copied from ../slow/ ;  couples', cList)
print("plot the sorted mean of firerate and std of firerate (red dots ind stim)")
print("begin time=%d, end time=%d"%(tbgn,tend))


# all trials
xsum = zeros(PN_number)
ysum = zeros(PN_number)
for ccc in cList:
    x = load_sf_avged_over_trial(ccc, 0, tbgn, tend)
    y = load_sf_stded_over_trial(ccc, 0, tbgn, tend)
    tuples = sorted(zip(x, y), reverse=True)
    xnew, ynew = array([t[0] for t in tuples]), array([t[1] for t in tuples]) # mean and error
    xsum += xnew
    ysum += ynew

xsum /= (1.0*cNum)
ysum /= (1.0*cNum)

#tuplet = sorted(zip(x, range(PN_number)), reverse=True)
#xodr = [t[1] for t in tuplet]

fill_between(x=range(PN_number), y1=smooth(xsum-1*ysum), y2=smooth(xsum+1*ysum), alpha=0.2, color="#089FFF", antialiased=true)
plot(xsum, color="white", lw=2)

#for i in range(PN_number):
    #if xodr[i] < PN_stim_number:
        #plot(i, xnew[i], '.', color='r', markersize=2)

xlabel("PN #")
ylabel("sorted fire rate (Hz)")
xlim([0,PN_number])
#ylim([0,50])
if cNum==1:
    savefig("sf_avg_c%d_var_%d_%d.jpg"%(cList[0], tbgn,tend))
    savefig("sf_avg_c%d_var_%d_%d.eps"%(cList[0], tbgn,tend))
show()
clf()
