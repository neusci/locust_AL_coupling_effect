execfile("../slow/slow_analy_head.py")
# execfile("../fast/fast_analy_head.py")

print('copied from ../prime/plot_ppcc_inc.py')

tbgn = 1100
tend = 1350 # real_end?
tlen = tend-tbgn
td = 50

print("Plot ppcc from each shift to shift0")


def get_an_odor_resp(c,tb,te,td=50):
    asf_trial_ls = array([[load_spec_sf_1trial(c,s,t,tb,te,td)
                           for t in range(ptTrial_number)]
                           for s in ptShift_list])
    # In [10]: shape(asf_trial_ls)
    # Out[10]: (20, 10, 830)
    #           20 shifts for the given couple,
    #           10 trials for each shift, and
    #           830 PNs for each trial...
    # ...
    ppcc_trial_ls = zeros([ptShift_number, ptTrial_number])
    asf_ref = 1.0*sum(asf_trial_ls[0],0)/ptTrial_number # center of shift0
    # ...
    for i in range(ptShift_number):
        for j in range(ptTrial_number):
            ppcc_trial_ls[i,j] = corr(asf_trial_ls[i,j], asf_ref)
    # ...
    ppcc_avg_ls=[avg(x) for x in ppcc_trial_ls]
    ppcc_std_ls=[std(x) for x in ppcc_trial_ls]
    return ppcc_avg_ls, ppcc_std_ls, ppcc_trial_ls


for couple in ptCouple_list:
    resp_avg, resp_std, _ = get_an_odor_resp(couple, tbgn, tend)
    odor_avg, odor_std, _ = get_an_odor_resp(odor_coupling, tbgn, tend)

    errorbar(x=odor_avg, y=resp_avg, xerr=odor_std, yerr=resp_std) #color='white'
    #fig_framin, fig_framax=-0.25,1.25
    fplot("y=x", [-0.2,1.2])
    #xlim([fig_framin,fig_framax])
    #ylim([fig_framin,fig_framax])
    xlabel("stimulation corr coef")
    ylabel("representation corr coef")
    savefig("ppcc_stim_vs_resp_c%d_%d_%d_%d.jpg"%(couple,tbgn,tend,td))
    savefig("ppcc_stim_vs_resp_c%d_%d_%d_%d.eps"%(couple,tbgn,tend,td))
    clf()
