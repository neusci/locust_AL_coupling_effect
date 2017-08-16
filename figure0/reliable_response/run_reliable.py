# !/usr/bin/env python
# -*- coding:utf-8 -*-

execfile('../../slow/slow_analy_head.py')

# this is from model_check
coupleID = 0

def mbin(x, th):
    if th<0: return
    x[x<=th]=0
    x[x>th]=1
    return x

for shiftID in shift_list:
    print(shiftID)
    t0 = array([mbin(load_sf_matrix(coupleID,shiftID,i,real_begin,real_end), 0)
                for i in range(trial_number)])
    #In [17]: shape(t0)
    #Out[17]: (10, 830, 130)

    t1 = mbin(sum(t0, 0), 0.66667*trial_number)
    resprate = 100.0*sum(t1, 0)/PN_number
    savetxt("./data/response_couple%d_shift%d.txt"%(coupleID,shiftID), resprate)
