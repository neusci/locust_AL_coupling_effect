#  !/usr/bin/env python
#  -*- coding:utf-8 -*-
execfile("../slow/slow_analy_head.py")

tlen=50 # 50 or 100. or 200? # 200 is not that good.
pridir=homedir+"prime_ppcc/"

# ---


def load_odorset_ad_avg(oset, st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_ad_avg_odorset%d_%d_%d_50.txt"%(oset, st, st+lt))


def load_odorset_ad_std(oset, st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_ad_std_odorset%d_%d_%d_50.txt"%(oset, st, st+lt))


def load_od_avg(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_od_avg_%d_%d_50.txt"%(st, st+lt))


def load_od_std(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_od_std_%d_%d_50.txt"%(st, st+lt))

# ---

if tlen == 50:
    x1=load_od_avg(1000, tlen)
    y10=load_odorset_ad_avg(0, 1000, tlen)
    y11=load_odorset_ad_avg(1, 1000, tlen)
    y12=load_odorset_ad_avg(2, 1000, tlen)
    y13=load_odorset_ad_avg(3, 1000, tlen)
    y14=load_odorset_ad_avg(4, 1000, tlen)

    x2=load_od_avg(1100, tlen)
    y20=load_odorset_ad_avg(0, 1100, tlen)
    y21=load_odorset_ad_avg(1, 1100, tlen)
    y22=load_odorset_ad_avg(2, 1100, tlen)
    y23=load_odorset_ad_avg(3, 1100, tlen)
    y24=load_odorset_ad_avg(4, 1100, tlen)

    x3=load_od_avg(1200, tlen)
    y30=load_odorset_ad_avg(0, 1200, tlen)
    y31=load_odorset_ad_avg(1, 1200, tlen)
    y32=load_odorset_ad_avg(2, 1200, tlen)
    y33=load_odorset_ad_avg(3, 1200, tlen)
    y34=load_odorset_ad_avg(4, 1200, tlen)

    x4=load_od_avg(1300, tlen)
    y40=load_odorset_ad_avg(0, 1300, tlen)
    y41=load_odorset_ad_avg(1, 1300, tlen)
    y42=load_odorset_ad_avg(2, 1300, tlen)
    y43=load_odorset_ad_avg(3, 1300, tlen)
    y44=load_odorset_ad_avg(4, 1300, tlen)

    plot(x1, y10, '.-', markersize=3) #, label="1000");
    plot(x1, y11, '.-', markersize=3) #, label="1000");
    plot(x1, y12, '.-', markersize=3) #, label="1000");
    plot(x1, y13, '.-', markersize=3) #, label="1000");
    plot(x1, y14, '.-', markersize=3) #, label="1000");
    plot(x2, y20, '.-', markersize=4) #, label="1100");
    plot(x2, y21, '.-', markersize=4) #, label="1100");
    plot(x2, y22, '.-', markersize=4) #, label="1100");
    plot(x2, y23, '.-', markersize=4) #, label="1100");
    plot(x2, y24, '.-', markersize=4) #, label="1100");
    plot(x3, y30, '.-', markersize=4) #, label="1200");
    plot(x3, y31, '.-', markersize=4) #, label="1200");
    plot(x3, y32, '.-', markersize=4) #, label="1200");
    plot(x3, y33, '.-', markersize=4) #, label="1200");
    plot(x3, y34, '.-', markersize=4) #, label="1200");
    plot(x4, y40, '.-', markersize=4) #, label="1300");
    plot(x4, y41, '.-', markersize=4) #, label="1300");
    plot(x4, y42, '.-', markersize=4) #, label="1300");
    plot(x4, y43, '.-', markersize=4) #, label="1300");
    plot(x4, y44, '.-', markersize=4) #, label="1300");

# --- ---

#fplot("y=x", [-1,1])
#legend(loc='lower right', prop={'size':10})
xlabel("Euclid distance between stimulus")
ylabel("Euclid distance between representation")
savefig("ppcc_odorset_%d.jpg"%tlen)
savefig("ppcc_odorset_%d.eps"%tlen)
show()
