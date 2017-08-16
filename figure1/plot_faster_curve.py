#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile('../slow/slow_analy_head.py')
print('Fig.2a of Wilson2007')
c=0
x=mean([load_sf_trial_avged(c  ,s,cd=50) for s in shift_list],0)
y=mean([load_sf_trial_avged(100,s,cd=50) for s in shift_list],0)

plot(x[20:40]/max(x[20:40]));
plot(y[20:40]/max(y[20:40]));
axvspan(2, 7, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
x1 = [0, 4, 8, 12, 16, 20]
labels1 = ['0','200','400','600','800','1000']
xticks(x1, labels1)  #, rotation='vertical')
xlabel('time from odor onset')
ylabel('fraction of maximum')
savefig('faster_curve.jpg')
savefig('faster_curve.eps')
clf()
