# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
#  in model checking, we can run this script in this way:
execfile("../slow/slow_analy_head.py")
for coupleID in ptCouple_list:
    for shiftID in ptShift_list:
        execfile("model_check.py")
"""

#coupleID = 333
#shiftID = 0
print(coupleID, shiftID)
tnumber = ptTrial_number

#=================================

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
vol_ls = [loaddata(coupleID,shiftID,i) for i in range(tnumber)]
PNavged_vol_ls = [1.0*sum(i,0)/PN_number for i in vol_ls]
spike_ls = map(vol_matrix_to_spike_matrix, vol_ls)


print("fluction ...")
figure()
plot(sum(vol_ls[0],0)/1000.0) # to mV
ylim([-55, -45])
xlim([0, 6000])
xlabel("time (ms)")
ylabel("voltage (mv)")
axvspan(22*50, 27*50, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
savefig("./model_check_data/fluction_%d_%d.jpg"%(coupleID,shiftID))
savetxt("./model_check_data/fluction_%d_%d.txt"%(coupleID,shiftID), sum(vol_ls[0],0)/1000.0)
clf()


print("response ...")
figure()
t0 = sum(map(vol_matrix_to_spike_timebin, vol_ls),0)
t1 = zeros(shape(t0))
t1[t0 <= (0.666*tnumber)]=0  # 6 responses in 9 trials in Laurent2005
t1[t0 >  (0.666*tnumber)]=1
plot(100.0*sum(t1, 0)/PN_number)
ylabel("response PN rate (%)")
x1 = [0, 40, 80, 120, 160, 200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
xlim([0, 140])
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
xlabel("time (ms)")
savefig("./model_check_data/response_%d_%d.jpg"%(coupleID,shiftID))
savetxt("./model_check_data/response_%d_%d.txt"%(coupleID,shiftID), 100.0*sum(t1, 0)/PN_number)
clf()


print("plotting bandpower...")
bp_ls = [thisBandpower(i) for i in PNavged_vol_ls]
figure()
bp=1.0*sum(bp_ls,0)/tnumber
plot(bp)
xlabel("time (ms)")
ylabel("bandpower")
x1 =      [0,       40,     80,    120,     160,    200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
xlim([0, 140])
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
savefig("./model_check_data/bandpower_%d_%d.jpg"%(coupleID,shiftID))
savetxt("./model_check_data/bandpower_%d_%d.txt"%(coupleID,shiftID), bp)
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
    savefig("./model_check_data/psd_%d_%d_%d.jpg"%(coupleID,shiftID,i))
    savetxt("./model_check_data/psd_fff_%d_%d_%d.txt"%(coupleID,shiftID,i), fff[:95])
    savetxt("./model_check_data/psd_ppp_%d_%d_%d.txt"%(coupleID,shiftID,i), ppp[:95])
    clf()


print("sorted ...")
figure()
# total spike number of all the PNs, in the time range that an odor appears
spike_avg1 = [1000.0*sum(i[:,sf_count_from:sf_count_to],1)/(sf_count_to-sf_count_from) for i in spike_ls]
ssa=sorted(sum(spike_avg1, 0)/tnumber, reverse=True)
plot(ssa)
xlabel("PN #")
ylabel("spike rate ($S^{-1}$)")
savefig("./model_check_data/sorted_%d_%d.jpg"%(coupleID,shiftID))
savetxt("./model_check_data/sorted_%d_%d.txt"%(coupleID,shiftID), ssa)
clf()


print("spike_rate ...")
# total spike number at all the run time, for each PN:
spike_avg0 = [1.0*sum(i, 0)/PN_number for i in spike_ls]
xls=map(mean, equally_divide(1000.0*sum(spike_avg0,0)/tnumber, sf_count_duration))
figure()
plot(xls)
x1 = [0, 40, 80, 120, 160, 200]
labels1 = ['0', '2000', '4000', '6000', '8000', '10000']
xticks(x1, labels1)  #, rotation='vertical')
xlim([0, 140])
xlabel("time (ms)")
ylabel("spike rate ($S^{-1}$)")
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
savefig("./model_check_data/spike_rate_%d_%d.jpg"%(coupleID,shiftID))  # _timebin
savetxt("./model_check_data/spike_rate_%d_%d.txt"%(coupleID,shiftID), xls)
clf()
