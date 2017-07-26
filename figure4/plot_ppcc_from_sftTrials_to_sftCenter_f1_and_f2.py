execfile("../slow/slow_analy_head.py")
# execfile("../fast/fast_analy_head.py")
print('copied from ../figure5_new/, revised for corr')

tb = 1100
te = 1350 # real_end?
tlen = te-tb
td = 50
print("Plot PPCC from each shift to each shift center (in matrix, trial avged)")

# --- --- --- --- --- --- ---

couple = 0
asf_trial_ls = array([[load_spec_sf_1trial(couple,s,t,tb,te,td) \
                        for t in range(trial_number)] for s in shift_list])
# In [10]: shape(asf_trial_ls)
# Out[10]: (20, 10, 830)
#           20 shifts for the given couple,
#           10 trials for each shift, and
#           830 PNs for each trial...
# ...

sftAvg_on_asf_trial_ls=[mean(asf_trial_ls[i], 0) for i in range(shift_number)]
# In [14]: shape(sftAvg_on_asf_trial_ls)


def ppcc_from_aShiftTrials_to_bShiftCenter_avg_std_ls(s0, s1):
    # this is based on the just loaded sftAvg_on_asf_trial_ls
    # for 2 given odors (defined by s0 and s1), compute ppcc between them
    thisTrials = asf_trial_ls[s0]
    thisCenter = sftAvg_on_asf_trial_ls[s1]
    edls = [corr(x,thisCenter) for x in thisTrials]
    return avg(edls), std(edls), edls

c = couple
ppcc_mat = zeros([shift_number, shift_number])
for i,j in itertools.product(range(shift_number), range(shift_number)):
    print("couple=%d, begin time=%d, end time=%d"%(c,tb,te),
          'shifts:', shift_list[i], shift_list[j])
    #if i > j: continue
    ppcc_mat[i,j] = ppcc_from_aShiftTrials_to_bShiftCenter_avg_std_ls(i, j)[0]

#for i,j in itertools.product(range(shift_number), range(shift_number)):
    #if i > j: ppcc_mat[i,j] = ppcc_mat[j,i]

savetxt("./data/ppcc_from_aShiftTrials_to_bShiftCenter_c%d_t%d_%d.txt"%(c,tb,te), ppcc_mat)

# --- --- --- --- --- --- ---

couple = 100
asf_trial_ls = array([[load_spec_sf_1trial(couple,s,t,tb,te,td) \
                        for t in range(trial_number)] for s in shift_list])
# In [10]: shape(asf_trial_ls)
# Out[10]: (20, 10, 830)
#           20 shifts for the given couple,
#           10 trials for each shift, and
#           830 PNs for each trial...
# ...

sftAvg_on_asf_trial_ls=[mean(asf_trial_ls[i], 0) for i in range(shift_number)]
# In [14]: shape(sftAvg_on_asf_trial_ls)


def ppcc_from_aShiftTrials_to_bShiftCenter_avg_std_ls(s0, s1):
    # this is based on the just loaded sftAvg_on_asf_trial_ls
    # for 2 given odors (defined by s0 and s1), compute ppcc between them
    thisTrials = asf_trial_ls[s0]
    thisCenter = sftAvg_on_asf_trial_ls[s1]
    edls = [corr(x,thisCenter) for x in thisTrials]
    return avg(edls), std(edls), edls

c = couple
ppcc_mat = zeros([shift_number, shift_number])
for i,j in itertools.product(range(shift_number), range(shift_number)):
    print("couple=%d, begin time=%d, end time=%d"%(c,tb,te),
          'shifts:', shift_list[i], shift_list[j])
    #if i > j: continue
    ppcc_mat[i,j] = ppcc_from_aShiftTrials_to_bShiftCenter_avg_std_ls(i, j)[0]

#for i,j in itertools.product(range(shift_number), range(shift_number)):
    #if i > j: ppcc_mat[i,j] = ppcc_mat[j,i]

savetxt("./data/ppcc_from_aShiftTrials_to_bShiftCenter_c%d_t%d_%d.txt"%(c,tb,te), ppcc_mat)

# --- --- --- --- --- --- ---

#subplot(121)
x=loadtxt('./data/ppcc_from_aShiftTrials_to_bShiftCenter_c0_t1100_1350.txt')
p=pcolormesh(x, vmin=-0.2, vmax=1.2, cmap="coolwarm")
#colorbar(p)
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c0_t%d_%d.jpg'%(tb,te))
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c0_t%d_%d.eps'%(tb,te))
clf()

#subplot(122)
y=loadtxt('./data/ppcc_from_aShiftTrials_to_bShiftCenter_c100_t1100_1350.txt')
q=pcolormesh(y, vmin=-0.2, vmax=1.2, cmap="coolwarm")
#colorbar(p)
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c100_t%d_%d.jpg'%(tb,te))
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c100_t%d_%d.eps'%(tb,te))
clf()

#subplot(121)
p=pcolormesh(x, vmin=-0.2, vmax=1.2, cmap="coolwarm")
colorbar(p)
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c0_t%d_%d_cbar.jpg'%(tb,te))
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c0_t%d_%d_cbar.eps'%(tb,te))
clf()

#subplot(122)
q=pcolormesh(y, vmin=-0.2, vmax=1.2, cmap="coolwarm")
colorbar(q)
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c100_t%d_%d_cbar.jpg'%(tb,te))
savefig('./ppcc_from_shiftTrials_to_shiftCenter_c100_t%d_%d_cbar.eps'%(tb,te))
clf()

z=zeros(shape(x))
z[x>y]=0.75
z[x<y]=0.25
p=pcolormesh(z, vmin=-0.2,vmax=1.2, cmap="coolwarm")
#colorbar(p)
savefig('./ppcc_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d.jpg'%(tb,te))
savefig('./ppcc_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d.eps'%(tb,te))
clf()

p=pcolormesh(z, vmin=-0.2,vmax=1.2, cmap="coolwarm")
colorbar(p)
savefig('./ppcc_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d_cbar.jpg'%(tb,te))
savefig('./ppcc_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d_cbar.eps'%(tb,te))
clf()
