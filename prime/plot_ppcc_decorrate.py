#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile("../slow/slow_analy_head.py")

tbgn=1000
tend=6400
tlen=50 # 50 or 100. or 200? # 200 is not that good.
pridir=homedir+"prime_ppcc/"

# ---

def load_ad_avg(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_ad_avg_%d_%d_50.txt"%(st, st+lt))


def load_ad_std(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_ad_std_%d_%d_50.txt"%(st, st+lt))


def load_od_avg(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_od_avg_%d_%d_50.txt"%(st, st+lt))


def load_od_std(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_od_std_%d_%d_50.txt"%(st, st+lt))

# ---

x =[load_od_avg(i, tlen) for i in range(tbgn,tend,tlen)]
dx=[load_od_std(i, tlen) for i in range(tbgn,tend,tlen)]
y =[load_ad_avg(i, tlen) for i in range(tbgn,tend,tlen)]
dy=[load_ad_std(i, tlen) for i in range(tbgn,tend,tlen)]

# https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.linregress.html
dec_rate=array([1.0*list(y[i]<x[i]).count(True)/len(x[i])  for i in rlen(x)]) # [0]: slope

plot(dec_rate, '.-', markersize=3) # , label="1000")
savetxt('ppcc_dec_rate.txt', dec_rate)
# legend(loc='lower right', prop={'size':10})
xticks(range(0, 101, 20), ['1000', '2000', '3000', '4000', '5000', '6000'])
xlabel("time (ms)")
ylabel("representing decorrelation rate")
#ylim([0,1])
savefig("dec_ppcc_resp_rate_time_%d.jpg"%tlen)
savefig("dec_ppcc_resp_rate_time_%d.eps"%tlen)
show()
clf()
