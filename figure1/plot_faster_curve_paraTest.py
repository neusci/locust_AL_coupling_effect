#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile('../slow/slow_analy_head.py')
print('Fig.2a of Wilson2007')


def plot_avg_std(x,xsem,coup,col):
    plot_begin,plot_end=20,40 # begin and end click on the figure
    errorbar(x=range(plot_end-plot_begin),
             y=x[plot_begin:plot_end]/max(x[plot_begin:plot_end]),
             yerr=xsem[plot_begin:plot_end]/max(x[plot_begin:plot_end]),
             color=col, linewidth=1.5, label=coup)


stim_avg_ls=[load_sf_trial_avged(100,s,cd=50) for s in ptShift_list]
stim_avg,stim_sem=mean(stim_avg_ls,0),std(stim_avg_ls,0)
savetxt('./stim_avg_100.txt', stim_avg)
savetxt('./stim_sem_100.txt', stim_sem)
plot_avg_std(stim_avg,stim_sem, label_ofc(100), color_ofc(100))

for c in ptCouple_list:
    print(c)
    resp_avg_ls=[load_sf_trial_avged(c  ,s,cd=50) for s in ptShift_list]
    resp_avg,resp_sem=mean(resp_avg_ls,0),std(resp_avg_ls,0)

    savetxt('./resp_avg_%d.txt'%c, resp_avg)
    savetxt('./resp_sem_%d.txt'%c, resp_sem)

    plot_avg_std(resp_avg,resp_sem, label_ofc(c), color_ofc(c))


axvspan(2, 7, facecolor='0.75', alpha=0.75) # ymax=0.1 # 22-27:100-350ms
legend()
xticks([0, 4, 8, 12, 16, 20], ['0','200','400','600','800','1000'])  #, rotation='vertical')
xlabel('time (ms)') #xlabel('time from odor onset')
ylabel('fraction of maximum')
savefig('faster_curve_paraTest.jpg')
savefig('faster_curve_paraTest.eps')
clf()
