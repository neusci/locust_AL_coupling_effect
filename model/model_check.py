# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
#  we can run this script in this way:
for coupleID in range(10): # 0--49
    for shiftID in [0, 2, 4, 6, 8, 10, 20, 40, 60, 80]:
        execfile("model_check.py")
"""

# be very careful on the below vars!!!
homedir = "/home/mw/"
execfile(homedir+".ipython/profile_default/startup/10-init.py")

# coupleID = 0  # 0--49 --- 99
shiftID = 0  # 0 2 4 6 8 10 20 40 60 80
tnumber = 20 # trial number
if_mc = True # if we are doing model check. if so, load different data..

PN_number = 830
LN_number = 300
time_begin = 500
time_end = 10500
stim_onset = 1000  # this is relative to time_{begin/end}
stim_offset = 3500
stim_rise = 400  # this is again relative to stim_{on/off}set
stim_decay = 6500
win_len = 100
win_step_len = 50
osc_begin = stim_onset+50
osc_end = stim_onset+300
osc_begin_win = int(floor((osc_begin/win_step_len))) # window number at osc begin
osc_end_win = int((floor(osc_end/win_step_len)))
power_lowerlimit = 15
power_upperlimit = 25
sampling_freq = 1000 # 1000 data per second
nfft_exp = 10 # 2**nfft_exp -> nfft

# vars controlling PN spike freq counting
sf_count_from = 1200 # stim_onset
sf_count_to = 1500   # stim_offset # this was from 1000ms till 1500ms
sf_count_duration = 50
timebin_len = 50

#=================================

def model_check_dir(t):
    """
      this function returns dir of model_check trials
      which are couple defined in coupleID, shift in shiftID, 20 trials
      Do run full time long!!!
    """
    if t >= tnumber:
        print("error in model_check_dir: max model_check trial number:", tnumber)
        return ""
    return "./%d/shift%d_trial%d/"%(coupleID, shiftID, t)


def cst_to_dir(c, s, t, model_check=False):
    # for model checking, a same dir saves everything
    if model_check: return model_check_dir(t) # c and s are just ignored!!
    if 0<=t<5:
        return "./%d/shift%d_trial%d/"%(c,s,t)
    elif 5<=t<10:
        return "./%d/shift%d_trial%d/"%(c,s,t)
    else:
        print("error in dir, trial number of which should be in [0,10]")
        return ""


def get_PN_fname(c,s,t, model_check=False):
    return cst_to_dir(c,s,t, model_check)+"doc_V_PN.txt"


def get_LN_fname(c,s,t, model_check=False):
    return cst_to_dir(c,s,t, model_check)+"doc_V_LN.txt"


def load_PN_data(c,s,t, model_check=False):
    return loadtxt(get_PN_fname(c,s,t, model_check))[time_begin+1:time_end+1,1:].T


def load_LN_data(c,s,t, model_check=False):
    return loadtxt(get_LN_fname(c,s,t, model_check))[time_begin+1:time_end+1,1:].T


def loaddata(c,s,t, model_check=False):
    return load_PN_data(c,s,t, model_check)


def thisBandpower(x):
    "def this to avoid the too long code line"
    return bandpower(x, sampling_freq, 2**nfft_exp, win_len, win_step_len, power_lowerlimit, power_upperlimit)


def vol_matrix_to_spike_matrix(a, th=0):
    """
      convert spike freq(sf) 2D matirx to spike time bins
       a is the sf matrix to be converted
       th is the threshold for detecting spikes
      returns the generated new matrix
      ... ...
      vol_matrix_to_spike_matrix(loadtxt("/home/mwang/neo_decorr0/0/PN_spike_freq_0_50.txt"))
    """
    if isinstance(a, list): a=array(a)
    b=zeros(shape(a))
    for i,j in muloop(shape(a)):
            if j ==0: continue
            if a[i, j-1]<=th and a[i,j]>th: b[i,j]=1
    return b


def count_spike_number_in_vol_list(a, th=0):
    """
      a is vol 1D array/list of a PN
    ...
      return the spike number in the above list
    ...
      a=loaddata(0,0,0)
      count_spike_number_in_vol_list(a[40])
      count_spike_number_in_vol_list(a[1, :1000])
      count_spike_number_in_vol_list(a[2, 1000:1500])
    """
    num = 0
    for i,x in enum(a):
        if i==0: continue
        if x>th and a[i-1]<=th: num += 1
    return num


def vol_matrix_to_spike_timebin(a, tblen=timebin_len, th=0, binary=True):
    """
      convert voltage fluction matirx to spike time bins
       a is the voltage matrix to be converted
       tblen is the length of time bins
       th is the threshold for detecting spikes
       binary is used to control what to count:
          True: only test is there is a spike in that bin
          False: count the detailed number of spikes in the bin
      returns the generated new matrix
      ... ...
      a=loaddata(0,0,0)
      b=vol_matrix_to_spike_timebin(a)
      pcolormesh(b); show()
    """
    b=zeros([shape(a)[0], int(floor(1.0*shape(a)[1]/tblen))])
    for i,j in muloop(shape(b)):
            b[i,j]=count_spike_number_in_vol_list(a[i, j*tblen:(j+1)*tblen], th)
    if binary: b[b>1]=1
    return b

#=================================

print("loading data ...")
vol_ls = [loaddata(coupleID,shiftID,i,if_mc) for i in range(tnumber)]
PNavged_vol_ls = [1.0*sum(i,0)/PN_number for i in vol_ls]
spike_ls = map(vol_matrix_to_spike_matrix, vol_ls)


print("fluction ...")
figure()
plot(sum(vol_ls[0],0)/1000.0) # to mV
ylim([-55, -45])
xlabel("time (ms)")
ylabel("voltage (mv)")
savefig("fluction_%d_%d.jpg"%(coupleID,shiftID))
clf()


print("response ...")
figure()
t0 = sum(map(vol_matrix_to_spike_timebin, vol_ls),0)
t1 = zeros(shape(t0))
t1[t0 <= (0.666*tnumber)]=0  # 6 responses in 9 trials in Laurent2005
t1[t0 >  (0.666*tnumber)]=1
plot(100.0*sum(t1, 0)/PN_number)
savetxt("response_%d_%d.txt"%(coupleID,shiftID), 100.0*sum(t1, 0)/PN_number)
xlabel("time (ms)")
ylabel("response PN rate (%)")
x1 = [0, 40, 80, 120, 160, 200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
savefig("response_%d_%d.jpg"%(coupleID,shiftID))
clf()


print("plotting bandpower...")
bp_ls = [thisBandpower(i) for i in PNavged_vol_ls]
figure()
plot(1.0*sum(bp_ls,0)/tnumber)
savetxt("bandpower_%d_%d.txt"%(coupleID,shiftID), 1.0*sum(bp_ls,0)/tnumber)
xlabel("time (ms)")
ylabel("bandpower")
x1 = [0, 40, 80, 120, 160, 200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
savefig("bandpower_%d_%d.jpg"%(coupleID,shiftID))
clf()


print("psd ...")
for i in muloop([tnumber]):
    print("\tprocessing PSD #", coupleID, shiftID, i)
    ppp, fff = myPSD(PNavged_vol_ls[i], sampling_freq, 2**nfft_exp)
    ppp[:5]=0
    figure()
    plot(fff[:95], ppp[:95])
    xlabel("frequence (Hz)")
    ylabel("PSD")
    savefig("psd_%d_%d_%d.jpg"%(coupleID,shiftID,i))
    clf()


print("sorted ...")
figure()
# total spike number of all the PNs, in the time range that an odor appears
spike_avg1 = [1000.0*sum(i[:,sf_count_from:sf_count_to],1)/(sf_count_to-sf_count_from) for i in spike_ls]
ssa=sorted(sum(spike_avg1, 0)/tnumber, reverse=True)
plot(ssa)
savetxt("sorted_%d_%d.txt"%(coupleID,shiftID), ssa)
xlabel("PN #")
ylabel("spike rate ($S^{-1}$)")
savefig("sorted_%d_%d.jpg"%(coupleID,shiftID))
clf()


print("spike_rate ...")
# total spike number at all the run time, for each PN:
spike_avg0 = [1.0*sum(i, 0)/PN_number for i in spike_ls]
xls=map(mean, equally_divide(1000.0*sum(spike_avg0,0)/tnumber, sf_count_duration))
figure()
plot(xls)
savetxt("spike_rate_%d_%d.txt"%(coupleID,shiftID), xls)
x1 = [0, 40, 80, 120, 160, 200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
xlabel("time (ms)")
ylabel("spike rate ($S^{-1}$)")
savefig("spike_rate_%d_%d.jpg"%(coupleID,shiftID))  # _timebin
clf()
