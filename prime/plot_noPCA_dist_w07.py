#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")
from itertools import combinations

print("this script compares fig with Fig.6b in wilson2007")
print("Sensory processing in the Drosophila antennal lobe, nat. neusci")

tick=array(range(PN_number))
#array([0,50,100,200,300,400,500,600,700,800])

def load_all_sf_at_momment(c,m0,m1):
    x = array([list(load_sf_avged_over_trial(c,s,m0,m1)) \
            for s in shift_list ])
    return x

def load_odor_sf_at_momment(m0,m1):
    return load_all_sf_at_momment(odor_coupling, m0, m1)


def noPC_dist(theCoup):
    dist_t_avg_ls = []
    dist_t_1q_ls = []
    dist_t_2q_ls = []
    dist_t_3q_ls = []
    #...
    idx =array(list(combinations(range(20), 2)))
    for t in range(real_begin, real_end, 50):
        #print(theCoup, t)
        distls=[]
        xtp=load_all_sf_at_momment(theCoup,t,t+50)
        for i in idx: distls.append(norm(xtp[i[0]]-xtp[i[1]], 2))
        distls = sort(distls)
        dist_t_avg_ls.append(avg(distls))
        l = len(distls)
        dist_t_1q_ls.append(distls[10])
        dist_t_2q_ls.append(distls[100])
        dist_t_3q_ls.append(distls[180])
        #dist_t_1q_ls.append(distls[int(round((1*l+1)/4.0))])
        #dist_t_2q_ls.append(distls[int(round((2*l+2)/4.0))])
        #dist_t_3q_ls.append(distls[int(round((3*l+3)/4.0))])
    return array(dist_t_avg_ls), array(dist_t_1q_ls), array(dist_t_2q_ls), array(dist_t_3q_ls)

def odor_noPC_dist():
    dist_t_avg_ls = []
    dist_t_1q_ls = []
    dist_t_2q_ls = []
    dist_t_3q_ls = []
    theCoup=odor_coupling
    #...
    idx =array(list(combinations(range(20), 2)))
    for t in range(real_begin, real_end, 50):
        #print(theCoup, t)
        distls=[]
        xtp=load_odor_sf_at_momment(t,t+50)
        for i in idx: distls.append(norm(xtp[i[0]]-xtp[i[1]], 2))
        distls = sort(distls)
        dist_t_avg_ls.append(avg(distls))
        l = len(distls)
        dist_t_1q_ls.append(distls[10])
        dist_t_2q_ls.append(distls[100])
        dist_t_3q_ls.append(distls[180])
        #dist_t_1q_ls.append(distls[int(round((1*l+1)/4.0))])
        #dist_t_2q_ls.append(distls[int(round((2*l+2)/4.0))])
        #dist_t_3q_ls.append(distls[int(round((3*l+3)/4.0))])
    return array(dist_t_avg_ls), array(dist_t_1q_ls), array(dist_t_2q_ls), array(dist_t_3q_ls)

#...

dist_t_avg_ls0, dist_t_1q_ls0, dist_t_2q_ls0, dist_t_3q_ls0 = noPC_dist(0)
#dist_t_avg_ls1, dist_t_1q_ls1, dist_t_2q_ls1, dist_t_3q_ls1 = PC_dist(1)
#dist_t_avg_ls2, dist_t_1q_ls2, dist_t_2q_ls2, dist_t_3q_ls2 = PC_dist(2)
#dist_t_avg_ls3, dist_t_1q_ls3, dist_t_2q_ls3, dist_t_3q_ls3 = PC_dist(3)
#dist_t_avg_ls4, dist_t_1q_ls4, dist_t_2q_ls4, dist_t_3q_ls4 = PC_dist(4)

## comment the following 3 groups, when only use 5 odorsets:
#dist_t_avg_ls5, dist_t_1q_ls5, dist_t_2q_ls5, dist_t_3q_ls5 = PC_dist(5)
#dist_t_avg_ls6, dist_t_1q_ls6, dist_t_2q_ls6, dist_t_3q_ls6 = PC_dist(6)
#dist_t_avg_ls7, dist_t_1q_ls7, dist_t_2q_ls7, dist_t_3q_ls7 = PC_dist(7)
#dist_t_avg_ls8, dist_t_1q_ls8, dist_t_2q_ls8, dist_t_3q_ls8 = PC_dist(8)
#dist_t_avg_ls9, dist_t_1q_ls9, dist_t_2q_ls9, dist_t_3q_ls9 = PC_dist(9)

#dist_t_avg_ls10, dist_t_1q_ls10, dist_t_2q_ls10, dist_t_3q_ls10 = PC_dist(10)
#dist_t_avg_ls11, dist_t_1q_ls11, dist_t_2q_ls11, dist_t_3q_ls11 = PC_dist(11)
#dist_t_avg_ls12, dist_t_1q_ls12, dist_t_2q_ls12, dist_t_3q_ls12 = PC_dist(12)
#dist_t_avg_ls13, dist_t_1q_ls13, dist_t_2q_ls13, dist_t_3q_ls13 = PC_dist(13)
#dist_t_avg_ls14, dist_t_1q_ls14, dist_t_2q_ls14, dist_t_3q_ls14 = PC_dist(14)

#dist_t_avg_ls15, dist_t_1q_ls15, dist_t_2q_ls15, dist_t_3q_ls15 = PC_dist(15)
#dist_t_avg_ls16, dist_t_1q_ls16, dist_t_2q_ls16, dist_t_3q_ls16 = PC_dist(16)
#dist_t_avg_ls17, dist_t_1q_ls17, dist_t_2q_ls17, dist_t_3q_ls17 = PC_dist(17)
#dist_t_avg_ls18, dist_t_1q_ls18, dist_t_2q_ls18, dist_t_3q_ls18 = PC_dist(18)
#dist_t_avg_ls19, dist_t_1q_ls19, dist_t_2q_ls19, dist_t_3q_ls19 = PC_dist(19)

odor_dist_t_avg_ls, odor_dist_t_1q_ls, odor_dist_t_2q_ls, odor_dist_t_3q_ls =\
    odor_noPC_dist()


#...

dist_t_avg_ls= dist_t_avg_ls0
dist_t_1q_ls = dist_t_1q_ls0
dist_t_2q_ls = dist_t_2q_ls0
dist_t_3q_ls = dist_t_3q_ls0


'''
dist_t_avg_ls= \
 (dist_t_avg_ls0+dist_t_avg_ls1+dist_t_avg_ls2+dist_t_avg_ls3+dist_t_avg_ls4)/5.0
dist_t_1q_ls = \
 (dist_t_1q_ls0+dist_t_1q_ls1+dist_t_1q_ls2+dist_t_1q_ls3+dist_t_1q_ls4)/5.0
dist_t_2q_ls = \
 (dist_t_2q_ls0+dist_t_2q_ls1+dist_t_2q_ls2+dist_t_2q_ls3+dist_t_2q_ls4)/5.0
dist_t_3q_ls = \
 (dist_t_3q_ls0+dist_t_3q_ls1+dist_t_3q_ls2+dist_t_3q_ls3+dist_t_3q_ls4)/5.0

# ...
dist_t_avg_ls= \
 (
 dist_t_avg_ls0+dist_t_avg_ls1+dist_t_avg_ls2+dist_t_avg_ls3+dist_t_avg_ls4+
 dist_t_avg_ls5+dist_t_avg_ls6+dist_t_avg_ls7+dist_t_avg_ls8+dist_t_avg_ls9+
 dist_t_avg_ls10+dist_t_avg_ls11+dist_t_avg_ls12+dist_t_avg_ls13+dist_t_avg_ls14+
 dist_t_avg_ls15+dist_t_avg_ls16+dist_t_avg_ls17+dist_t_avg_ls18+dist_t_avg_ls19
  )/20.0

dist_t_1q_ls = \
 (
 dist_t_1q_ls0+ dist_t_1q_ls1 +dist_t_1q_ls2 +dist_t_1q_ls3 +dist_t_1q_ls4+
 dist_t_1q_ls5+ dist_t_1q_ls6 +dist_t_1q_ls7 +dist_t_1q_ls8 +dist_t_1q_ls9+
 dist_t_1q_ls10+dist_t_1q_ls11+dist_t_1q_ls12+dist_t_1q_ls13+dist_t_1q_ls14+
 dist_t_1q_ls15+dist_t_1q_ls16+dist_t_1q_ls17+dist_t_1q_ls18+dist_t_1q_ls19
 )/20.0

dist_t_2q_ls = \
 (
 dist_t_2q_ls0+ dist_t_2q_ls1 +dist_t_2q_ls2 +dist_t_2q_ls3 +dist_t_2q_ls4+
 dist_t_2q_ls5+ dist_t_2q_ls6 +dist_t_2q_ls7 +dist_t_2q_ls8 +dist_t_2q_ls9+
 dist_t_2q_ls10+dist_t_2q_ls11+dist_t_2q_ls12+dist_t_2q_ls13+dist_t_2q_ls14+
 dist_t_2q_ls15+dist_t_2q_ls16+dist_t_2q_ls17+dist_t_2q_ls18+dist_t_2q_ls19
 )/20.0

dist_t_3q_ls = \
 (
 dist_t_3q_ls0+ dist_t_3q_ls1 +dist_t_3q_ls2 +dist_t_3q_ls3 +dist_t_3q_ls4+
 dist_t_3q_ls5+ dist_t_3q_ls6 +dist_t_3q_ls7 +dist_t_3q_ls8 +dist_t_3q_ls9+
 dist_t_3q_ls10+dist_t_3q_ls11+dist_t_3q_ls12+dist_t_3q_ls13+dist_t_3q_ls14+
 dist_t_3q_ls15+dist_t_3q_ls16+dist_t_3q_ls17+dist_t_3q_ls18+dist_t_3q_ls19
 )/20.0
'''

#plot(dist_t_avg_ls)
plot(dist_t_1q_ls)
plot(dist_t_2q_ls)
plot(dist_t_3q_ls)
xlabel("time (ms)")
ylabel("distances")
x1 = [0,20, 40,60, 80,100, 120, 140 ]
labels1 = ['0','1000', '2000','3000', '4000','5000', '6000', '7000']
xticks(x1, labels1)  #, rotation='vertical')
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
#show()
savefig('all_noPC_vg_3qs.jpg');
clf()

#plot(odor_dist_t_avg_ls)
plot(odor_dist_t_1q_ls)
plot(odor_dist_t_2q_ls)
plot(odor_dist_t_3q_ls)
xlabel("time (ms)")
ylabel("distances")
x1 = [0,20, 40,60, 80,100, 120, 140 ]
labels1 = ['0','1000', '2000','3000', '4000','5000', '6000', '7000']
xticks(x1, labels1)  #, rotation='vertical')
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
#show()
savefig('all_noPC_odor_avg_3qs.jpg');
clf()

plot(dist_t_1q_ls, '.-')
plot(odor_dist_t_1q_ls)
xlabel("time (ms)")
ylabel("distances")
x1 = [0,20, 40,60, 80,100, 120, 140 ]
labels1 = ['0','1000', '2000','3000', '4000','5000', '6000', '7000']
xticks(x1, labels1)  #, rotation='vertical')
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
#ylim([0,10])
#show()
savefig('all_noPC_1stq.jpg');
clf()