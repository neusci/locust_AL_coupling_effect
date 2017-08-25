#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile('../slow/slow_analy_head.py')
print('Fig.2a of Wilson2007')

c=0

stim_avg_ls=[load_sf_trial_avged(100,s,cd=50) for s in shift_list]
resp_avg_ls=[load_sf_trial_avged(c  ,s,cd=50) for s in shift_list]

stim_avg,stim_sem=mean(stim_avg_ls,0),std(stim_avg_ls,0)
resp_avg,resp_sem=mean(resp_avg_ls,0),std(resp_avg_ls,0)

'''
line(dark) fill(lite)
crimson    pink/green lime
purple     violet
'''


def plot_avg_std(x,xsem,c1,c2,m):
    fill_between(x=range(20),
                 y1=(x[20:40]-xsem[20:40])/max(x[20:40]),
                 y2=(x[20:40]+xsem[20:40])/max(x[20:40]),
                 alpha=0.5, facecolor=c2)
    # errorbar(x, y, yerr=yerr, fmt='o-')
    plot(#x=range(20), y=
         x[20:40]/max(x[20:40]),
         marker=m, markersize=4.5,
         color=c1, linewidth=1.5)

axvspan(2, 7, ymax=0.1, facecolor='0.75', alpha=0.75) # 21-27:50-350ms => 100-400ms

#plot_avg_std(stim_avg,stim_sem,'crimson', 'pink',   'X');
plot_avg_std(stim_avg,stim_sem,'green', 'lime',   'X');
plot_avg_std(resp_avg,resp_sem,'purple','violet', 'o');

xticks([0, 4, 8, 12, 16, 20], ['0','200','400','600','800','1000'])  #, rotation='vertical')
xlabel('time from odor onset')
ylabel('fraction of maximum')
savefig('faster_curve.jpg')
savefig('faster_curve.eps')
show()

'''
stim_avg_ls=[]
stim_std_ls=[]
resp_avg_ls=[]
resp_std_ls=[]

for s in shift_list:
    #...
    print(s)
    stim_avg_it, stim_std_it=load_sf_trial_avg_std(100,s,cd=50)
    resp_avg_it, resp_std_it=load_sf_trial_avg_std(c  ,s,cd=50)
    stim_avg_ls.append(stim_avg_it)
    stim_std_ls.append(stim_std_it) # not used
    resp_avg_ls.append(resp_avg_it) # not used
    resp_std_ls.append(resp_std_it)
'''
