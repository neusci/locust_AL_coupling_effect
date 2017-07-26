#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

c,s,t=3,0,0
plot(sum(loaddata(c,s,t), 0)[1000:2000]/1000.0)
axvspan(50, 350, facecolor='0.5', alpha=0.5)
xlabel('time from odor onset (ms)')
ylabel('voltage oscillation (mv)')
savefig('an_osc.jpg')
savefig('an_osc.eps')
clf()
