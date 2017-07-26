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
x_slp=array([stats.linregress(x[i],y[i])[0]  for i in rlen(x)]) # [0]: slope
x_err=array([stats.linregress(x[i],y[i])[4]  for i in rlen(x)]) # [-1]:stderr
y_slp=array([stats.linregress(x[i],y[i])[0]  for i in rlen(y)]) # rlen(x)==rlen(y)...
y_err=array([stats.linregress(x[i],y[i])[4]  for i in rlen(y)])

fill_between(x=rlen(y_slp), y1=y_slp-y_err, y2=y_slp+y_err, alpha=0.2, antialiased=true) #, color="#089FFF"
plot(y_slp, '.-', markersize=3) # , label="1000")
savetxt('ppcc_slope.txt', y_slp)
# legend(loc='lower right', prop={'size':10})
xticks(range(0, 101, 20), ['1000', '2000', '3000', '4000', '5000', '6000'])
xlabel("time (ms)")
ylabel("representing ppcc slope")
#ylim([0,1])
savefig("slp_ppcc_resp_time_%d.jpg"%tlen)
savefig("slp_ppcc_resp_time_%d.eps"%tlen)
show()
clf()

'''
plot(y_slp/x_slp, '.-', markersize=3) #, label="1000"); # minux - is better???
# legend(loc='lower right', prop={'size':10})
xticks(range(0, 101, 20), ['1000', '2000', '3000', '4000', '5000', '6000'])
xlabel("time (ms)")
ylabel("ppcc slope ratio")
#ylim([0,5])
savefig("slp_ppcc_resp_stim_ratio_%d.jpg"%tlen)
savefig("slp_ppcc_resp_stim_ratio_%d.eps"%tlen)
clf()
show()
'''
