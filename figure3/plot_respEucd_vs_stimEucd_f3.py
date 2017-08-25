execfile("../slow/slow_analy_head.py")
# execfile("../fast/fast_analy_head.py")

print('copied from ../prime/plot_eucD_inc.py')

tbgn = 1100
tend = 1350 # real_end?
tlen = tend-tbgn
td = 50
couple = 0

print("Plot euc distance from each shift to shift0")


def get_an_odor_resp(c,tb,te,td=50):
    asf_trial_ls = array([[load_spec_sf_1trial(c,s,t,tb,te,td) \
                           for t in range(trial_number)] for s in shift_list])
    # In [10]: shape(asf_trial_ls)
    # Out[10]: (20, 10, 830)
    #           20 shifts for the given couple,
    #           10 trials for each shift, and
    #           830 PNs for each trial...
    # ...
    dis_trial_ls = zeros([shift_number, trial_number])
    asf_ref = 1.0*sum(asf_trial_ls[0],0)/trial_number # center of shift0
    # ...
    for i in range(shift_number):
        for j in range(trial_number):
            dis_trial_ls[i,j] = norm(asf_trial_ls[i,j]-asf_ref)
    # ...
    dis_avg_ls=[avg(x) for x in dis_trial_ls]
    dis_std_ls=[std(x) for x in dis_trial_ls]
    return dis_avg_ls, dis_std_ls, dis_trial_ls


resp_avg, resp_std, _ = get_an_odor_resp(couple, tbgn, tend)
odor_avg, odor_std, _ = get_an_odor_resp(odor_coupling, tbgn, tend)
errorbar(x=odor_avg, y=resp_avg, xerr=odor_std, yerr=resp_std) #color='white'

fig_len=500
fplot("y=x", [0,fig_len])
xlim([0,fig_len])
ylim([0,fig_len])
xlabel("stimulation distance")
ylabel("representation distance")
savefig("eucd_stim_vs_resp_%d_%d_%d.jpg"%(tbgn,tend,td))
savefig("eucd_stim_vs_resp_%d_%d_%d.eps"%(tbgn,tend,td))
clf()
