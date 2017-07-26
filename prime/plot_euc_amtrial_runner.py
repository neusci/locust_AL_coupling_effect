#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")
tlen=50 # length for each counting period
td=50 # load sf50 files

print("this script is used to run plot_euc_enlarge_among_trials.py in batch")
print("tlen=%d, td=%d", tlen, td)
print("You may need to comment tbgn,tend,tlen,td in plot_euc_enlarge_among_trials.py first!")
print("CHECK again!!!")

for tbgn in range(real_begin,real_end,tlen):
    tend=tbgn+tlen
    print(tbgn, tend, datetime_str())
    execfile("plot_euc_enlarge_among_trials.py")
