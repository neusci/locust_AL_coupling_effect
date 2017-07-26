#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile('../slow/slow_analy_head.py')

slist=shift_list
offnet=array([load_sf_avged_over_trial(100,i,1100,1350,50) for i in slist])
onnet =array([load_sf_avged_over_trial(  0,i,1100,1350,50) for i in slist])


n_groups = shift_number #number of odors
index = arange(n_groups)
bar_width = 0.4
opacity = 0.4
error_config = {'ecolor': '0.3'}

# http://matplotlib.org/examples/pylab_examples/barchart_demo.html
for i in range(PN_number):
    print(i)

    rects1 = bar(index-bar_width/2, offnet[:,i], bar_width,
                    alpha=opacity, color='b',
                    #yerr=std_men, error_kw=error_config,
                    label='offnet')

    rects2 = bar(index+bar_width/2, onnet[:,i], bar_width,
                    alpha=opacity, color='r',
                    #yerr=std_women, error_kw=error_config,
                    label='onnet')

    xlabel('odor #')
    ylabel('firing rate (Hz)')
    xticks(range(20), array(range(20))+1)
    ylim([0,40])
    legend()

    savefig('./fig/off2onnet_selectivity_PN%d.jpg'%i)
    savefig('./fig/off2onnet_selectivity_PN%d.eps'%i)
    clf()
