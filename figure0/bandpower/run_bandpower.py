#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

#couple_number=5 # use 5 couples only?
for coupleID in range(couple_number):
    for shiftID in shift_list:
        print("current couple and shift:", coupleID, shiftID)
        vol_ls = [loaddata(coupleID,shiftID,i) for i in range(trial_number)]
        PNavged_vol_ls = [1.0*sum(i,0)/PN_number for i in vol_ls]
        bp_ls = [thisBandpower(i) for i in PNavged_vol_ls]
        bp_this = 1.0*sum(bp_ls,0)/trial_number
        savetxt("./data/bandpower_%dms_%d_%d.txt"%(win_len,coupleID,shiftID), bp_this)
        """
        figure()
        plot(bp_this)
        ylabel("bandpower")
        x1 = [0, 40, 80, 120, 160, 200]
        labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
        xticks(x1, labels1)  #, rotation='vertical')
        axvspan(21, 26, facecolor='0.5', alpha=0.5)
        savefig("./data/bandpower_%d_%d.jpg"%(coupleID,shiftID))
        clf()
        """
