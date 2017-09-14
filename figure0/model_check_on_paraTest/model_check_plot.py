# !/usr/bin/env python
# -*- coding:utf-8 -*-

execfile("../../slow/slow_analy_head.py")

reminder =  """
#  in model checking, we can run this script in this way:
execfile("../slow/slow_analy_head.py")
for coupleID in ptCouple_list:
    for shiftID in ptShift_list:
        execfile("model_check.py")
"""

print('run `model_check.py` in this way, before running this script:')
print(reminder)
print('fluction and sorted are not plotted here')


for coupleID in ptCouple_list:
    print(coupleID)
    bp_list = []
    psd_list = []
    rsp_list = []
    sp_list = []

    for shiftID in ptShift_list:
        # bandpower
        bp_list.append(loadtxt("./model_check_data/bandpower_%d_%d.txt"%(coupleID,shiftID)))
        # psd
        psd_list_temp = []
        for i in muloop([ptTrial_number]):
            psd_list_temp.append(loadtxt("./model_check_data/psd_ppp_%d_%d_%d.txt"%(coupleID,shiftID,i)))
        psd_list.append( mean(psd_list_temp, 0) )
        # response
        rsp_list.append(loadtxt("./model_check_data/response_%d_%d.txt"%(coupleID,shiftID)))
        # firerate
        sp_list.append(loadtxt("./model_check_data/spike_rate_%d_%d.txt"%(coupleID,shiftID)))

    # now plot it (for the current coupling):
    plot(mean(bp_list,0));
    xlabel("time (ms)")
    ylabel("bandpower")
    xticks([0, 40, 80, 120], ['0', '2000', '4000', '6000'])
    xlim([0, 140])
    axvspan(22, 27, facecolor='0.5', alpha=0.5)
    savefig("./model_check_fig/bandpower_%d.jpg"%(coupleID))
    savefig("./model_check_fig/bandpower_%d.eps"%(coupleID))
    clf()

    plot(mean(psd_list,0));
    xlabel("frequence (Hz)")
    ylabel("PSD")
    savefig("./model_check_fig/psd_%d.jpg"%(coupleID))
    savefig("./model_check_fig/psd_%d.eps"%(coupleID))
    clf()

    plot(mean(rsp_list,0));
    ylabel("response PN rate (%)")
    xticks([0, 40, 80, 120], ['0', '2000', '4000', '6000'])
    xlim([0, 140])
    axvspan(22, 27, facecolor='0.5', alpha=0.5)
    xlabel("time (ms)")
    savefig("./model_check_fig/response_%d.jpg"%(coupleID))
    savefig("./model_check_fig/response_%d.eps"%(coupleID))
    clf()

    plot(mean(sp_list,0));
    xticks([0, 40, 80, 120], ['0', '2000', '4000', '6000'])
    xlim([0, 140])
    xlabel("time (ms)")
    ylabel("spike rate ($S^{-1}$)")
    axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
    savefig("./model_check_fig/spike_rate_%d.jpg"%(coupleID))  # _timebin
    savefig("./model_check_fig/spike_rate_%d.eps"%(coupleID))  # _timebin
    clf()
