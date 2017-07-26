#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile("../slow/slow_analy_head.py")

tlen=50 # 50 or 100. or 200? # 200 is not that good.
pridir=homedir+"prime_euc/"

# ---

def load_ad_avg(st, lt): #start time, length of time period
    return loadtxt(pridir+"euc_ad_avg_%d_%d_50.txt"%(st, st+lt))


def load_ad_std(st, lt): #start time, length of time period
    return loadtxt(pridir+"euc_ad_std_%d_%d_50.txt"%(st, st+lt))


def load_od_avg(st, lt): #start time, length of time period
    return loadtxt(pridir+"euc_od_avg_%d_%d_50.txt"%(st, st+lt))


def load_od_std(st, lt): #start time, length of time period
    return loadtxt(pridir+"euc_od_std_%d_%d_50.txt"%(st, st+lt))

# ---

x =[load_od_avg(i, tlen) for i in range(1000,6400,tlen)]
dx=[load_od_std(i, tlen) for i in range(1000,6400,tlen)]
y =[load_ad_avg(i, tlen) for i in range(1000,6400,tlen)]
dy=[load_ad_std(i, tlen) for i in range(1000,6400,tlen)]

x_avg=array([mean(i)       for i in x])
x_scp=array([max(i)-min(i) for i in x])
y_avg=array([mean(i)       for i in y])
y_scp=array([max(i)-min(i) for i in y])

fill_between(x=rlen(y_avg), y1=y_avg-y_scp, y2=y_avg+y_scp, alpha=0.2, antialiased=true) #, color="#089FFF"
plot(y_avg, '.-', markersize=3) # , label="1000")
# legend(loc='lower right', prop={'size':10})
xticks(range(0, 101, 20), ['1000', '2000', '3000', '4000', '5000', '6000'])
xlabel("time (ms)")
ylabel("Euclid distance between representation")
savefig("euc_resp_time_%d.jpg"%tlen)
savefig("euc_resp_time_%d.eps"%tlen)
show()
clf()


plot(y_avg/x_avg, '.-', markersize=3) #, label="1000"); # minux - is better???
# legend(loc='lower right', prop={'size':10})
xticks(range(0, 101, 20), ['1000', '2000', '3000', '4000', '5000', '6000'])
xlabel("time (ms)")
ylabel("Euclid distance ratio")
savefig("euc_resp_stim_ratio_%d.jpg"%tlen)
savefig("euc_resp_stim_ratio_%d.eps"%tlen)
show()
