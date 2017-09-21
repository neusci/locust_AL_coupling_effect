# !/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys


if os.path.exists('/home/mwang'): # working on 32-cores cluster
    homedir = "/home/mwang/"
    execfile(homedir+".ipython/profile_default/startup/10-init.py")
    print("working on 32-cores in the home dir:", homedir)
elif os.path.exists('/home/mw'):  # working on PCs
    homedir = "/media/mw/seagate20170619/32cores/"  # USB-HDD!
    # try to use PC local py-init script, first..
    if os.path.exists("/home/mw/.ipython/profile_default/startup/10-init.py"):
        execfile("/home/mw/.ipython/profile_default/startup/10-init.py")
    elif os.path.exists(homedir+".ipython/profile_default/startup/10-init.py"):
        execfile(homedir+".ipython/profile_default/startup/10-init.py")
    else:
        print("ipy-init script not found! quitting")
        sys.exit()
    # ...
    print("working on PC in the home dir:", homedir)
elif os.path.exists('/home/mogei'):
    homedir = "/home/mogei/" #homedir = "/media/mw/seagate20170619/32cores/"
    execfile(homedir+".ipython/profile_default/startup/10-init.py")
    print("working on 12-cores in the home dir:", homedir)
else:  # WTF?
    # homesir have NOT been defined in this case, cannot go on.
    print("homedir not set! quitting")
    sys.exit()


# be very careful on the below vars!!!
analy_time_begin=1100 # the period that fast osc. is very strong!
analy_time_end=1350   # ^^^   from 1.1S to 1.35S,
PN_resp_thres=25 # PN with firing rate alrger than this is active

couple_number = 1 # use only 1 couple now and means testX in parameter test!
#ptCouple_list = [111,112,113,121,122,123,131,132,133,
#                 211,212,213,221,222,223,231,232,233,
#                 311,312,313,321,322,323,331,332,333,]

#ptCouple_list = [222,223,232,233, 322,323,332,333,] # combos
#ptCouple_list = [600,601,602,603,604,605,606] # coupling
#ptCouple_list = [700,701,702,703,704,705,706] # fast GABA
ptCouple_list = [800,801,802,803,804,805,806] # slow GABA

ptCouple_number = len(ptCouple_list)

trial_number = 10
ptTrial_number = 5 # !!! parameter test !!!

PN_number = 830
LN_number = 300
PN_stim_number = 120
LN_stim_number = 120
time_begin = 500
time_end = 7000 # this 7000 is in fact 6500, since the first 500 is cut off
real_begin = 0
real_end = time_end-time_begin
stim_onset = 1000  # this is real, and is relative to time_{begin/end}
stim_offset = 3500 # this also is real
stim_rise = 400  # this is again relative to stim_{on/off}set
stim_decay = 6500
win_len = 50
win_step_len = 50
osc_begin = stim_onset+100 # in this period the oscillation is strong!
osc_end = stim_onset+350
osc_begin_win = int(floor((1.0*osc_begin/win_step_len))) # window number at osc begin
osc_end_win = int((floor(1.0*osc_end/win_step_len)))

power_lowerlimit = 15
power_upperlimit = 25
sampling_freq = 1000 # 1000 data per second
nfft_exp = 10 # 2**nfft_exp -> nfft

#shift_list = range(0,PN_stim_number,int(round(1.0*PN_stim_number/shift_number)))
# do not use shift1..5, which are useless, althoug well runned
shift_list = [0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114]
ptShift_list = [0,12,24,36,48]  # !!! parameter test !!!

# [0,2,4,6,8,10,20,40,60,80]  # olds: j = int(floor(2**(jjj-1)))
shift_number = len(shift_list) # int(round(0.5*PN_stim_number/shift_list_step))
ptShift_number = len(ptShift_list) # int(round(0.5*PN_stim_number/shift_list_step))

odor_coupling = 100
odor_list = [array(range(PN_stim_number+i)[i:]) for i in shift_list]
ptOdor_list = [array(range(PN_stim_number+i)[i:]) for i in ptShift_list]

def odor_IDs(x): return odor_list[shift_list.index(x)]
def ptOdor_IDs(x): return ptOdor_list[ptShift_list.index(x)]


timebin_len = 50
# vars controlling PN spike freq counting
sf_count_from = osc_begin
sf_count_to = osc_end
sf_count_duration = 50
sfcd_list = [5, 50]  # generate sf files with sf_count_duration being 5 or 50

#=================================

def type_of_couple(c):
    """
        if c is a test id in parameter test
        or it is a old-school coupling id
    """
    if c in ptCouple_list:
        return 1
    elif 0 <= c <= 100: # 100-odor; 99-old-model-check; no more than 100!
        return 0
    else:
        return -1


def trial_number_for_couple(c):
    # the correct trial number for c
    if type_of_couple(c) == 1:
        return ptTrial_number
    elif type_of_couple(c)==0:
        return trial_number
    else:
        print("you are using a bad coupling/testID", c)
        return 0


def cst_to_dir(c, s, t):
    if type_of_couple(c) == 1:
        datadir = homedir+"neodecParaTest/"  # !!! parameter test !!!
    elif type_of_couple(c)==0:
        datadir = homedir+"neodec/"  # !!! parameter test !!!
    else:
        print("you are using a bad coupling/testID", c)
        # datadir has not been defined in this branch!!
    return datadir+"%d/shift%d_trial%d/"%(c,s,t)


def get_PN_fname(c,s,t):
    return cst_to_dir(c,s,t)+"doc_V_PN.txt"


def get_LN_fname(c,s,t):
    return cst_to_dir(c,s,t)+"doc_V_LN.txt"


def load_PN_data(c,s,t):
    return loadtxt(get_PN_fname(c,s,t))[time_begin+1:time_end+1,1:].T


def load_LN_data(c,s,t):
    return loadtxt(get_LN_fname(c,s,t))[time_begin+1:time_end+1,1:].T


def loaddata(c,s,t):
    return load_PN_data(c,s,t)


def load_PN2PN_matrix(c,s=0,t=0):
    return loadtxt(cst_to_dir(c,s,t)+'mat_PN2PN_nACH.txt')


def load_PN2LN_matrix(c,s=0,t=0):
    return loadtxt(cst_to_dir(c,s,t)+'mat_PN2LN_nACH.txt')


def load_LN2PN_matrix(c,s=0,t=0):
    return loadtxt(cst_to_dir(c,s,t)+'mat_LN2PN_slow.txt')


def load_LN2PN_matrix_fast(c,s=0,t=0):
    return loadtxt(cst_to_dir(c,s,t)+'mat_LN2PN_GABA.txt')


def load_LN2LN_matrix(c,s=0,t=0):
    return loadtxt(cst_to_dir(c,s,t)+'mat_LN2LN_GABA.txt')


def color_ofc(cc):  # line/points color of given couple
    if cc==0:
        return 'purple'
    elif cc==100:
        return 'green'
    else:
        c = type_of_couple(cc)*1000+mod(cc,100)
        if   c==1006:
            return 'saddlebrown'
        elif c==1005:
            return 'darkgoldenrod'
        elif c==1004:
            return 'red'
        elif c==1003: # this is the intact version
            return 'purple'
        elif c==1002:
            return 'blue'
        elif c==1001:
            return 'olive'
        else       : #1000 or others
            return 'black'


couple_tune_labels = ['x0.3', 'x0.5', 'x0.8', 'intact(1)', 'x1.4', 'x1.6', 'x2']
GABA_tune_labels   = ['x0.1', 'x0.3', 'x0.5', 'intact(1)', 'x2'  , 'x3'  , 'x10']


def label_ofc(cc,typ='couple'):  # line/points label of given couple
    if cc==0: # neodec cases
        return 'intact(1)'
    elif cc==100:
        return 'decouple(0)'
    else:
        c = mod(cc,100)
        if typ=='couple':
            return couple_tune_labels[c]
        elif typ=='GABA':
            return GABA_tune_labels[c]
        else:
            print("ERROR in calling label_ofc - wrong type provided - use couple or GABA")
            return 'Error'


def thisBandpower(x):
    "def this to avoid the too long code line"
    return bandpower(x, sampling_freq, 2**nfft_exp, win_len, win_step_len, power_lowerlimit, power_upperlimit)


def vol_matrix_to_spike_matrix(a, th=0):
    """
      convert voltage 2D matirx to spike matrix
       a is the vol matrix to be converted
       th is the threshold for detecting spikes
      returns the generated new matrix
      ... ...
      vol_matrix_to_spike_matrix(loaddata(0,0,0))
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
      returns the new generated matrix
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


def vol_matrix_sum_to_timebin(a, tblen=timebin_len):
    """
      convert voltage fluction matirx to voltage fluction time bins
       a is the voltage matrix to be converted
       tblen is the length of time bins
      returns the new generated matrix
      ... ...
       a=loaddata(2,0,0)[:,1100:3500]
       b=vol_matrix_sum_to_timebin(a, 10)
       s=vol_matrix_to_spike_timebin(a, 10)
       plot(sum(b,0), sum(s,0), '.'); show()
    """
    b=zeros([shape(a)[0], int(floor(1.0*shape(a)[1]/tblen))])
    for i,j in muloop(shape(b)): b[i,j]=sum(a[i, j*tblen:(j+1)*tblen])
    return b


def count_sf_from_spike_matrix(a, tbgn,tend):
    """
      this function is to calculate the spike numbers of each neuron in the
        time period defined by [tbgn, tend].
      input:
          a is a spike matrix (usual converted from vol matrix)
          tbgn and tend are two intergers indicating the time in ms.
      ...
      return an array, with each item representing a spike freq of a neuron
      ...
      x=vol_matrix_to_spike_matrix(loaddata(c,s,t), th)
      count_sf_from_spike_matrix(x, 1000, 1500)
    """
    return sum(a[:,tbgn:tend],1)


def generate_sf_file(c, s, t, cf=real_begin, ct=real_end, cd=sf_count_duration, ifPN=True):
    """
      This func generates a set of files recording the spike freq of each PN
        of the specific give couple(c), shift(s) and trial(t)
      The generated file will be in the same dir as the vol files
      ...
      return nothing (side effect --- files generated!)
      NOTE:  this func is usually use together with load_sf_xxx()
      ...
      # an useful example:
        for i in range(couple_number):
            for j in shift_list:  # 0,2,4,6,8, 10, 20, 40, 60, 80
                for k in range(trial_number):
                    generate_sf_file(i, j, k)
                    generate_sf_file(i, j, k, ifPN=False)
      # an example on using the files (without load_sf_xxx)
      aaa = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1200_1250.txt")+randn(PN_number)
      bbb = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1250_1300.txt")+randn(PN_number)
      slope, intercept, r_value, p_value, std_err = stats.linregress(aaa, bbb)
      plot(aaa, bbb, '.'); title(r_value);
      xlim([-5,65]); ylim([-5,65]);
      xlabel("prev"); ylabel("next");
      savefig("t.jpg"); show()
      # ...
      # yet another example
      aaa = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1200_1250.txt")+randn(PN_number)
      bbb = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1250_1300.txt")+randn(PN_number)
      ccc = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1300_1350.txt")+randn(PN_number)
      ddd = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1350_1400.txt")+randn(PN_number)
      x=(aaa+bbb)/2.0
      y=(ccc+ddd)/2.0
      plot(x,y,'.'); show()
      x=(aaa+bbb+ccc)/3.0
      y=(bbb+ccc+ddd)/3.0
      plot(x,y,'.'); show()
      plot((aaa+bbb+ccc+ddd)/4.0, loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq.txt")[:,1], '.'); show()
    """
    if not (cd in set(sfcd_list)):
        print("Error in calling load_sf_file: cd is not in sfcd list:", sfcd_list)
        return -1
    # ...
    if ifPN:
        data = loaddata(c, s, t)
        print('\t'+cst_to_dir(c, s, t)+"PN_spike_freq_*_(*+%d).txt"%cd)
        for ttt in range(cf, ct, cd):
            fob = open(cst_to_dir(c, s, t)+"PN_spike_freq_%d_%d.txt"%(ttt,(ttt+cd)), 'w')
            for n in range(PN_number):
                if ttt>0:
                    count=count_spike_number_in_vol_list(data[n, (ttt-1):(ttt+cd)])
                elif ttt==0:
                    count=count_spike_number_in_vol_list(data[n, ttt:(ttt+cd)])
                else:
                    print("Error in calling generate_sf_file: cf<0")
                fob.write(str(count/(cd/1000.0))+'\n')
            fob.close()
    else: # then LN:
        data = load_LN_data(c, s, t)
        print('\t'+cst_to_dir(c, s, t)+"LN_spike_freq_*_(*+%d).txt"%cd)
        for ttt in range(cf, ct, cd):
            fob = open(cst_to_dir(c, s, t)+"LN_spike_freq_%d_%d.txt"%(ttt,(ttt+cd)), 'w')
            for n in range(LN_number):
                if ttt>0:
                    count=count_spike_number_in_vol_list(data[n, (ttt-1):(ttt+cd)], th=-20)
                elif ttt==0:
                    count=count_spike_number_in_vol_list(data[n, ttt:(ttt+cd)], th=-20)
                else:
                    print("Error in calling generate_sf_file: cf<0")
                fob.write(str(count/(cd/1000.0))+'\n')
            fob.close()


def load_sf_from_file(c,s,t, cf, ct, cd=sf_count_duration, ifPN=True):
    """
      This func reads spike freq files generated by generate_sf_file()
        c, s, and t are couple, shift, and trial, as above
        cf and ct are count from and count to
      ...
      return an array of PN_number size, item of which is spike freq of each PN
      ...
      # an example of using this
      a=load_sf_from_file(0,0,0, 1100,3500)
      b=load_sf_from_file(0,0,1, 1100,3500)
      slope, intercept, r_value, p_value, std_err = stats.linregress(a, b)
      print(r_value)
      plot(a, b, '.')
      show()
    """
    if ifPN:
        NN_number=PN_number
    else:
        NN_number=LN_number
    #
    sf_sum = zeros(NN_number)
    count_num = int(floor(1.0*(ct-cf)/cd))
    #
    if cf < real_begin:
        print("Error in calling load_sf_file: cf is less than %d!"%sf_count_from)
        return sf_sum
    # ...
    if ct > real_end:
        print("Error in calling load_sf_file: ct is larger than %d!"%sf_count_to)
        return sf_sum
    # ...
    if not (cd in set(sfcd_list)):
        print("Error in calling load_sf_file: cd is not in sfcd list:", sfcd_list)
        return sf_sum
    # ...
    if mod(ct, cd) != 0 or mod(cf, cd) != 0:
        print("Error in calling load_sf_file: cf/ct is not at x*%d!"%cd)
        return sf_sum
    # ...
    if ifPN:
        for i in cf+array(range(count_num))*cd:
            sf_sum += loadtxt(cst_to_dir(c,s,t)+"PN_spike_freq_%d_%d.txt"%(i,i+cd))
    else:
        for i in cf+array(range(count_num))*cd:
            sf_sum += loadtxt(cst_to_dir(c,s,t)+"LN_spike_freq_%d_%d.txt"%(i,i+cd))
    return 1.0*sf_sum/count_num


def load_sf_in_trial(c,s,t, cd=sf_count_duration, ifPN=True):
    """
      This func reads whole time line spike freq (avg sf of all neurons) from files
        c, s, and t are couple, shift, and trial, as above
      ...
      return an array of (real_end-real_begin)/cd size,
         item of which is spike freq of each timebin (or cd)
      ...
      # an example of using this
      plot(load_sf_in_trial(0,0,0))
      show()
    """
    if ifPN:
        NN_number=PN_number
    else:
        NN_number=LN_number
    #
    ret=zeros([NN_number, int(round(1.0*(real_end-real_begin)/cd))])
    #
    for i,x in enum(range(real_begin, real_end, cd)):
        ret[:,i]=load_sf_from_file(c, s, t, x, x+cd, cd, ifPN)
    return 1.0*sum(ret,0)/NN_number


def load_sf_trial_avged(c,s, cd=sf_count_duration, ifPN=True):
    """
      This func computes trial-averaged whole time line spike freq from files
        c and s are couple and shift as above
      ...
      return an array of (real_end-real_begin)/cd size,
         item of which is the averaged spike freq in each timebin (or cd)
      ...
      # an example of using this
      plot(load_sf_trial_avged(0,0,0))
      show()
    """
    l = int(round(1.0*(real_end-real_begin)/cd))
    # ...
    this_trial_number = trial_number_for_couple(c)
    # ...
    ret=zeros([this_trial_number, l])# the trial_number dim will be avged/stded
    for i in range(this_trial_number):
        ret[i,:]=load_sf_in_trial(c,s,i,cd, ifPN)
    return array([mean(ret[:,j]) for j in range(l)])


def load_sf_trial_stded(c,s, cd=sf_count_duration, ifPN=True):
    """
      This func computes whole time line spike freq trial-std from files
        c and s are couple and shift as above
      ...
      return an array of (real_end-real_begin)/cd size,
         item of which is the spike freq std in each timebin (or cd)
      ...
      # an example of using this
        c=0
        s=0
        l = int(round((real_end-real_begin)/cd))
        a=load_sf_trial_avged(c,s,cd,ifPN)
        d=load_sf_trial_stded(c,s,cd,ifPN)
        fill_between(x=range(l), y1=(a-2*d), y2=(a+2*d), alpha=0.2, color="#089FFF", antialiased=true)
        plot(a, color="white", lw=2)
        show()
    """
    l = int(round((real_end-real_begin)/cd))
    # ...
    this_trial_number = trial_number_for_couple(c)
    # ...
    ret=zeros([this_trial_number, l])# the trial_number dim will be avged/stded
    for i in range(this_trial_number):
        ret[i,:]=load_sf_in_trial(c,s,i,cd, ifPN)
    return array([std(ret[:,j]) for j in range(l)])


def load_sf_trial_avg_std(c,s, cd=sf_count_duration, ifPN=True):
    """
      Same with load_sf_trial_avg_std and load_sf_trial_avg_std
        only that both avg and std are returned
      return array is of (real_end-real_begin)/cd size
    """
    l = int(round(1.0*(real_end-real_begin)/cd))
    # ...
    this_trial_number = trial_number_for_couple(c)
    # ...
    ret=zeros([this_trial_number, l])# the trial_number dim will be avged/stded
    for i in range(this_trial_number):
        ret[i,:]=load_sf_in_trial(c,s,i,cd, ifPN)
    return array([mean(ret[:,j]) for j in range(l)]), array([std(ret[:,j]) for j in range(l)])


def load_sf_matrix(c,s,t, cf,ct, cd=sf_count_duration, ifPN=True):
    """
      This func reads spike freq files generated by generate_sf_file()
        c and s are couple and shift
        cf and ct are count from and count to
      ...
      return a matrix of NN_number x timebin_number shape
             item of which is spike freq of that PN in that timebin.
      ...
      # an example of using this
        x=load_sf_matrix(0,0,0,0,6500)
        pcolormesh(x)
        show()
    """
    if ifPN:
        NN_number=PN_number
    else:
        NN_number=LN_number
    #
    timebin_number = int(round(1.0*(ct-cf)/cd))
    m=zeros([NN_number, timebin_number])
    for i,x in enum(range(cf,ct,cd)):
        m[:,i]=load_sf_from_file(c,s,t, x,x+cd,cd, ifPN)
    return m


def load_sf_avged_over_trial(c,s, cf, ct, cd=sf_count_duration, ifPN=True):
    """
      This func reads spike freq files generated by generate_sf_file()
        c and s are couple and shift
        cf and ct are count from and count to
      ...
      return an array of NN_number size, item of which is spike freq of each PN averaged over trials
      ...
      # an example of using this
      a=load_sf_avged_over_trial(0,0, 1100,3500)
      b=load_sf_avged_over_trial(0,2, 1100,3500)
      slope, intercept, r_value, p_value, std_err = stats.linregress(a, b)
      print(r_value)
      plot(a, b, '.')
      show()
    """
    if ifPN:
        NN_number=PN_number
    else:
        NN_number=LN_number
    # ...
    this_trial_number = trial_number_for_couple(c)
    # ...
    x=array([load_sf_from_file(c,s,t,cf,ct,cd, ifPN) for t in range(this_trial_number)])
    return array([mean(x[:,i]) for i in range(NN_number)])

'''
def load_sf_stded_over_trial(c,s, cf, ct, cd=sf_count_duration, ifPN=True):
    """
      This func reads spike freq files generated by generate_sf_file()
        c and s are couple and shift
        cf and ct are count from and count to
      ...
      return an array of PN_number size, item of which is spike freq of each PN averaged over trials
      ...
      # an example of using this
      x=load_sf_avged_over_trial(0,0, 1100,3500)
      y=load_sf_stded_over_trial(0,0, 1100,3500)
      tuples = sorted(zip(x, y), reverse=True)
      x, y = [t[0] for t in tuples], [t[1] for t in tuples]
      plot(x)
      plot(y, '.')
      show()
    """
    if ifPN:
        NN_number=PN_number
    else:
        NN_number=LN_number
    # ...
    this_trial_number = trial_number_for_couple(c)
    # ...
    x=array([load_sf_from_file(c,s,t,cf,ct,cd, ifPN) for t in range(this_trial_number)])
    return array([std(x[:,i]) for i in range(NN_number)])
'''


""" try to improve the above function names >>>>
    all the following functions return a 1d list/array (not 2d matrix)
    temp functions return array of size = (real_end-real_begin)/timebin_num
    spec functions return array of size = NN_number """


def load_temp_sf_1trial(c,s,t, cd=sf_count_duration, ifPN=True):
    return load_sf_in_trial(c,s,t, cd, ifPN)


def load_temp_sf_trial_avged(c,s, cd=sf_count_duration, ifPN=True):
    return load_sf_trial_avged(c, s, cd, ifPN)


def load_temp_sf_trial_stded(c,s, cd=sf_count_duration, ifPN=True):
    return load_sf_trial_stded(c, s, cd, ifPN)


def load_spec_sf_1trial(c,s,t, cf, ct, cd=sf_count_duration, ifPN=True):
    return load_sf_from_file(c,s,t, cf, ct, cd, ifPN)


def load_spec_sf_trial_avged(c,s, cf, ct, cd=sf_count_duration, ifPN=True):
    return load_sf_avged_over_trial(c,s, cf, ct, cd, ifPN)

'''
def load_spec_sf_trial_stded(c,s, cf, ct, cd=sf_count_duration, ifPN=True):
    return load_sf_stded_over_trial(c,s, cf, ct,cd, ifPN)
'''
# end of name refinement <<<<


def load_odor_sf_from_file(s,t,cf=analy_time_begin,ct=analy_time_end, cd=sf_count_duration,c=odor_coupling, ifPN=True):
    '''
      loads odor representing PN firing rates
    '''
    return load_sf_from_file(odor_coupling,s,t, cf, ct,cd, ifPN)


def load_odor_sf_avged_over_trial(s,cf=analy_time_begin,ct=analy_time_end, cd=sf_count_duration,c=odor_coupling, ifPN=True):
    '''
      loads odor representing PN firing rates --- avged
    '''
    return load_sf_avged_over_trial(odor_coupling,s, cf, ct,cd, ifPN)

"""
def load_odor_sf_stded_over_trial(s,cf=analy_time_begin,ct=analy_time_end, cd=sf_count_duration,c=odor_coupling, ifPN=True):
    '''
      loads odor representing PN firing rates --- stded
    '''
    return load_sf_stded_over_trial(odor_coupling,s, cf, ct,cd, ifPN)
"""

def load_odor_spec_sf_trial_avged(s,cf=analy_time_begin,ct=analy_time_end, cd=sf_count_duration,c=odor_coupling, ifPN=True):
    return load_odor_sf_avged_over_trial(odor_coupling,s, cf, ct, cd, ifPN)

"""
def load_odor_spec_sf_trial_stded(s,cf=analy_time_begin,ct=analy_time_end, cd=sf_count_duration,c=odor_coupling, ifPN=True):
    return load_odor_sf_stded_over_trial(odor_coupling,s, cf, ct, cd, ifPN)
"""


# ------


def comp_eucd_from_sf(c0,s0,t0,c1,s1,t1,cf,ct,cd=sf_count_duration, ifPN=True):
    """
      this function computes distance between of PN fire rates of 2 trials
        c s t are couple shift trail number
        cf and ct are count from and count to
      ...
      returns a float indicating the distance
    """
    a=load_sf_from_file(c0,s0,t0,cf,ct,cd,ifPN)
    b=load_sf_from_file(c1,s1,t1,cf,ct,cd,ifPN)
    return norm(a-b)


def comp_ppcc_from_sf(c0,s0,t0,c1,s1,t1,cf,ct,cd=sf_count_duration, ifPN=True):
    """
      this function computes ppcc between of PN fire rates of 2 trials
        c s t are couple shift trail number
        cf and ct are count from and count to
      ...
      returns a float indicating the ppcc
    """
    a=load_sf_from_file(c0,s0,t0,cf,ct,cd,ifPN)
    b=load_sf_from_file(c1,s1,t1,cf,ct,cd,ifPN)
    return corrcoef([a,b])[0,1] # 00:aa,11:bb,01:ab,10:ba


'''
def filter_active_NN_from_sf(c,s, th, cf,ct,cd=sf_count_duration, ifPN=True):
    """
      this function read sf files, and filters PNs that spike more active (>=) than threshold
        c and s are couple and shift
        cf and ct are count from and count to
      ...
      returns an array containing the active PN ids
      # ...
      aa=filter_active_NN_from_sf(0,0, 1100,3500, 15)
      bb=filter_active_NN_from_sf(0,4, 1100,3500, 15)
      print("for couple 0, shift 0 odor corresponds to PN set", aa)
      print("for couple 0, shift 4 odor corresponds to PN set", bb)
      xx=sets_divergence(aa,bb)
      print("for couple 0 trial 0, shift 4 in odor leads to %s in response"%xx)
    """
    a=load_sf_avged_over_trial(c, s, cf, ct, cd, ifPN)
    return array([i for i,x in enum(a) if x>=th])


def filter_inactive_NN_from_sf(c,s, th, cf,ct, cd=sf_count_duration, ifPN=True):
    """
      this function read sf files, and filters PNs that spike less (<=) active than threshold
        c and s are couple and shift
        cf and ct are count from and count to
      ...
      returns an array containing the active PN ids
      # ...
      aa=filter_active_NN_from_sf(0,0, 1100,3500, 15)
      bb=filter_active_NN_from_sf(0,4, 1100,3500, 15)
      print("for couple 0, shift 0 odor corresponds to PN set", aa)
      print("for couple 0, shift 4 odor corresponds to PN set", bb)
      xx=sets_divergence(aa,bb)
      print("for couple 0 trial 0, shift 4 in odor leads to %s in response"%xx)
    """
    a=load_sf_avged_over_trial(c, s, cf, ct, cd, ifPN)
    return array([i for i,x in enum(a) if x<=th])


def filter_active_NN_from_sf_1trial(c,s,t, th, cf,ct,cd=sf_count_duration, ifPN=True):
    """
      this function read sf files, and filters PNs that spike more active (>=) than threshold
        c s t are couple shift trail number
        cf and ct are count from and count to
      ...
      returns an array containing the active PN ids
    """
    a=load_sf_from_file(c,s,t,cf,ct,cd, ifPN)
    return array([i for i,x in enum(a) if x>=th])


def filter_inactive_NN_from_sf_1trial(c,s,t, th, cf,ct,cd=sf_count_duration, ifPN=True):
    """
      this function read sf files, and filters PNs that spike less (<=) active than threshold
        c s t are couple shift trail number
        cf and ct are count from and count to
      ...
      returns an array containing the active PN ids
    """
    a=load_sf_from_file(c,s,t,cf,ct,cd, ifPN)
    return array([i for i,x in enum(a) if x<=th])
'''

'''
def comp_sets_diverg_from_sf(c0,s0,t0, c1,s1,t1, th, tb,te,cd=sf_count_duration, ifPN=True):
    """
      this function computes the divergence between the representing PN sets of 2 trials
        c s t are couple shift trail number
        cf and ct are count from and count to
        th is the threshold
      ...
      returns an int indicating the divergence
    """
    x0=filter_active_NN_from_sf_1trial(c0,s0,t0, th, tb,te,cd, ifPN)
    x1=filter_active_NN_from_sf_1trial(c1,s1,t1, th, tb,te,cd, ifPN)
    return sets_divergence(x0, x1)


def count_barrier_jumper_from_sf(c0,s0,t0,c1,s1,t1,th, cf,ct,cd=sf_count_duration,ifPN=True):
    """
      this function regards threshold region as a barrier, and
           counts how many PNs have jumped through it in various trials
        c s t are couple shift trail number
        cf and ct are count from and count to
      ...
      returns an int indicating the number of PNs that are different sides of th in the two trials
    """
    a=load_sf_from_file(c0,s0,t0,cf,ct,cd,ifPN)
    b=load_sf_from_file(c1,s1,t1,cf,ct,cd,ifPN)
    a[a<=th]=0
    a[a>th]=1
    b[b<=th]=0
    b[b>th]=1
    return sum(abs(a-b))/2.0
'''
