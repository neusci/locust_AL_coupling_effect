execfile("../slow/slow_analy_head.py")
# execfile("../fast/fast_analy_head.py")
print('copied from ../prime/plot_eucD_inc.py')

tb = 1100
te = 1350 # real_end?
tlen = te-tb
td = 50
print("Plot euc distance from each shift to each shift center (in matrix, trial avged)")

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
# I believe that, the answer should be (20, 830)

def eucd_from_aShiftTrials_to_bShiftCenter_avg_std_ls(s0, s1):
    # this is based on the just loaded sftAvg_on_asf_trial_ls
    # for 2 given odors (defined by s0 and s1), compute eucd between them
    thisTrials = asf_trial_ls[s0]
    thisCenter = sftAvg_on_asf_trial_ls[s1]
    edls = [norm(x-thisCenter) for x in thisTrials]
    return avg(edls), std(edls), edls

c = couple
eucd_mat = zeros([shift_number, shift_number])
for i,j in itertools.product(range(shift_number), range(shift_number)):
    print("couple=%d, begin time=%d, end time=%d"%(c,tb,te),
          'shifts:', shift_list[i], shift_list[j])
    #if i > j: continue  # not symmetrical, cannot skip!!!
    eucd_mat[i,j] = eucd_from_aShiftTrials_to_bShiftCenter_avg_std_ls(i, j)[0]

#for i,j in itertools.product(range(shift_number), range(shift_number)):
#    if i > j: eucd_mat[i,j] = eucd_mat[j,i]

savetxt("./data/eucd_from_aShiftTrials_to_bShiftCenter_c%d_t%d_%d.txt"%(c,tb,te), eucd_mat)

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


def eucd_from_aShiftTrials_to_bShiftCenter_avg_std_ls(s0, s1):
    # this is based on the just loaded sftAvg_on_asf_trial_ls
    # for 2 given odors (defined by s0 and s1), compute eucd between them
    thisTrials = asf_trial_ls[s0]
    thisCenter = sftAvg_on_asf_trial_ls[s1]
    edls = [norm(x-thisCenter) for x in thisTrials]
    return avg(edls), std(edls), edls

c = couple
eucd_mat = zeros([shift_number, shift_number])
for i,j in itertools.product(range(shift_number), range(shift_number)):
    print("couple=%d, begin time=%d, end time=%d"%(c,tb,te),
          'shifts:', shift_list[i], shift_list[j])
    #if i > j: continue
    eucd_mat[i,j] = eucd_from_aShiftTrials_to_bShiftCenter_avg_std_ls(i, j)[0]

#for i,j in itertools.product(range(shift_number), range(shift_number)):
#    if i > j: eucd_mat[i,j] = eucd_mat[j,i]

savetxt("./data/eucd_from_aShiftTrials_to_bShiftCenter_c%d_t%d_%d.txt"%(c,tb,te), eucd_mat)

# --- --- --- --- --- --- ---

x=loadtxt('./data/eucd_from_aShiftTrials_to_bShiftCenter_c0_t1100_1350.txt')
y=loadtxt('./data/eucd_from_aShiftTrials_to_bShiftCenter_c100_t1100_1350.txt')

#subplot(121)
p=pcolormesh(x, vmin=50, vmax=400, cmap="coolwarm")
savefig('./eucd_from_shiftTrials_to_shiftCenter_c0_t%d_%d.jpg'%(tb,te))
savefig('./eucd_from_shiftTrials_to_shiftCenter_c0_t%d_%d.eps'%(tb,te))
clf()

#subplot(122)
q=pcolormesh(y, vmin=50, vmax=400, cmap="coolwarm")
savefig('./eucd_from_shiftTrials_to_shiftCenter_c100_t%d_%d.jpg'%(tb,te))
savefig('./eucd_from_shiftTrials_to_shiftCenter_c100_t%d_%d.eps'%(tb,te))
clf()

#subplot(121)
p=pcolormesh(x, vmin=50, vmax=400, cmap="coolwarm")
colorbar(p)
savefig('./eucd_from_shiftTrials_to_shiftCenter_c0_t%d_%d_cbar.jpg'%(tb,te))
savefig('./eucd_from_shiftTrials_to_shiftCenter_c0_t%d_%d_cbar.eps'%(tb,te))
clf()

#subplot(122)
q=pcolormesh(y, vmin=50, vmax=400, cmap="coolwarm")
colorbar(q)
savefig('./eucd_from_shiftTrials_to_shiftCenter_c100_t%d_%d_cbar.jpg'%(tb,te))
savefig('./eucd_from_shiftTrials_to_shiftCenter_c100_t%d_%d_cbar.eps'%(tb,te))
clf()

z=zeros(shape(x))
z[x>y]=0.75
z[x<y]=0.25
p=pcolormesh(z, vmin=-1,vmax=2, cmap="coolwarm")
savefig('./eucd_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d.jpg'%(tb,te))
savefig('./eucd_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d.eps'%(tb,te))
clf()

z=zeros(shape(x))
z[x>y]=0.75
z[x<y]=0.25
p=pcolormesh(z, vmin=-1,vmax=2, cmap="coolwarm")
colorbar(p)
savefig('./eucd_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d_cbar.jpg'%(tb,te))
savefig('./eucd_from_shiftTrials_to_shiftCenter_0vs100_t%d_%d_cbar.eps'%(tb,te))
clf()
