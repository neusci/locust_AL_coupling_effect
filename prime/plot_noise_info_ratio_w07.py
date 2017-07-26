#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile("../slow/slow_analy_head.py")

print("this script plots the noise-info-ratio as Fig.1 in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")


def avg_std_at_moment(c,s,m):
    # return the mean of avg&std of each neuron at [m,m+50]
    #x = zeros([trial_number, PN_stim_number]) #PN_number # only the stimed
    x = array([load_sf_from_file(c,s,i,m,m+50)[odor_IDs(s)] \
                 for i in range(trial_number)])
    x0 = [avg(x[:,j]) for j in range(PN_stim_number)] # PN_number
    x1 = [std(x[:,j]) for j in range(PN_stim_number)]
    return mean(x0), mean(x1), 1.0*mean(x1)/mean(x0)


def avg_std_of_cs(c,s):
    x=array([avg_std_at_moment(c,s,i) for i in range(real_begin,real_end,50)])
    return x[:,0], x[:,1], x[:,2]

# load postsynaptic (on network) firing rates
x0=zeros((real_end-real_begin)/50.0) # avg at each timebin
x1=zeros((real_end-real_begin)/50.0) # std at each timebin
x2=zeros((real_end-real_begin)/50.0) # std/avg at each timebin

for c in range(couple_number):
    for s in shift_list:
        print(c,s)
        xt = avg_std_of_cs(c,s)
        x0 += xt[0]
        x1 += xt[1]
        x2 += xt[2]

x0 /= (1.0*couple_number*shift_number)
x1 /= (1.0*couple_number*shift_number)
x2 /= (1.0*couple_number*shift_number)


# load presynaptic (off network) firing rates
q0=zeros((real_end-real_begin)/50.0) # odor avg at each timebin
q1=zeros((real_end-real_begin)/50.0) # odor std at each timebin
q2=zeros((real_end-real_begin)/50.0) # odor std/avg at each timebin

c = odor_coupling
for s in shift_list:
    print(c,s)
    qt = avg_std_of_cs(c,s)
    q0 += qt[0]
    q1 += qt[1]
    q2 += qt[2]

q0 /= (1.0*shift_number)
q1 /= (1.0*shift_number)
q2 /= (1.0*shift_number)


# save to txt
savetxt("avg-resp-noise-info-ratio.txt", x0)
savetxt("std-resp-noise-info-ratio.txt", x1)
savetxt("std-div-avg-resp-noise-info-ratio.txt", x2)
savetxt("avg-stim-noise-info-ratio.txt", q0)
savetxt("std-stim-noise-info-ratio.txt", q1)
savetxt("std-div-avg-stim-noise-info-ratio.txt", q2)


'''
# plot with the saved data
x0=loadtxt("avg-resp-noise-info-ratio.txt")
x1=loadtxt("std-resp-noise-info-ratio.txt")
q0=loadtxt("avg-stim-noise-info-ratio.txt")
q1=loadtxt("std-stim-noise-info-ratio.txt")
'''


# plots -- Fig1 in Wilson2007
plot(x0, '.-');
plot(q0, '.-');
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
xticks1 = [0, 20, 40, 60, 80, 100, 120, 140]
labels1 = ['0', '1000', '2000', '3000', '4000', '5000', '6000', '7000']
xticks(xticks1, labels1)  #, rotation='vertical')
xlabel('time (ms)')
ylabel('mean')
savefig('avg.jpg');
savefig('avg.eps');
clf()


plot(x1, '.-');
plot(q1, '.-');
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
xticks1 = [0, 20, 40, 60, 80, 100, 120, 140]
labels1 = ['0', '1000', '2000', '3000', '4000', '5000', '6000', '7000']
xticks(xticks1, labels1)  #, rotation='vertical')
xlabel('time (ms)')
ylabel('std.')
savefig('std.jpg');
savefig('std.eps');
clf()


plot(x2, '.-'); # need to be loaded first. do it before runing this code!
plot(q2, '.-');
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
xticks1 = [0, 20, 40, 60, 80, 100, 120, 140]
labels1 = ['0', '1000', '2000', '3000', '4000', '5000', '6000', '7000']
xticks(xticks1, labels1)  #, rotation='vertical')
xlabel('time (ms)')
ylabel('std./mean')
savefig('noise-info-ratio.jpg');
savefig('noise-info-ratio.eps');
clf()


# plots -- Fig2 in Wilson2007
plot(x0[20:40]/max(x0[20:40]), '.-'); # from odor onset, plot 1 second
plot(q0[20:40]/max(q0[20:40]), '.-');
axvspan(2, 7, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
xticks1 = [0, 5, 10, 15, 20]
labels1 = ['0', '250', '500', '750', '1000']
xticks(xticks1, labels1)  #, rotation='vertical')
xlabel('time from odor onset (ms)')
ylabel('fraction of maximum')
savefig('peak-norm-avg.jpg');
savefig('peak-norm-avg.eps');
clf()
