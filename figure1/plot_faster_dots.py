#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile('../slow/slow_analy_head.py')
print('Fig.2d of Wilson2007 (dots version)')

c=0
tprd=5 # period length, let cd=tprd

xlist=[]
ylist=[]


for s in shift_list:
    print('\n odor (shift)', s)
    for t in range(trial_number):
        print('\t trial', t)
        x=load_sf_in_trial(c  , s, t, cd=tprd)
        y=load_sf_in_trial(100, s, t, cd=tprd)
        # ...
        xlist.append( tprd*( list(x).index(max(x)) ) - 1000 ) # odor onset at 1th-Second
        ylist.append( tprd*( list(y).index(max(y)) ) - 1000 )


for li,lx in enum(xlist):
    if lx>2500:
        xlist[li]=nan

for li,lx in enum(ylist):
    if lx>2500:
        ylist[li]=nan


plot(rand(len(xlist)), xlist, '.', c='r')
plot(rand(len(ylist))+1.5, ylist, '.', c='b')
axhline(y=350, color='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
axhline(y=100, color='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
#x1 = [0, 4, 8, 12, 16, 20]
#labels1 = ['0','200','400','600','800','1000']
xticks([], [])  #, rotation='vertical')
#xlabel('time from odor onset')
ylabel('fraction of maximum')
savefig('faster_dots.jpg')
savefig('faster_dots.eps')
clf()
