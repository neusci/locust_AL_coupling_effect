execfile("../slow/slow_analy_head.py")

tbgn=1200
tend=1500 # 3500?
sf_min=5
sf_max=35

print("plot firerate std for each firerate mean")
print("begin time=%d, end time=%d"%(tbgn,tend))

c=0  # couple
s=0  # shift
std_ls0=[0]
for th in range(sf_min,sf_max):
    s0=set(filter_active_PN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_PN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        std_ls0.append(std_ls0[-1])
    else:
        ss=array(list(s0-s1))
        std_ls0.append(mean(load_sf_stded_over_trial(c,s,tbgn,tend)[ss]))


c=1  # couple
s=0  # shift
std_ls1=[0]
for th in range(sf_min,sf_max):
    s0=set(filter_active_PN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_PN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        std_ls1.append(std_ls1[-1])
    else:
        ss=array(list(s0-s1))
        std_ls1.append(mean(load_sf_stded_over_trial(c,s,tbgn,tend)[ss]))


c=2  # couple
s=0  # shift
std_ls2=[0]
for th in range(sf_min,sf_max):
    s0=set(filter_active_PN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_PN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        std_ls2.append(std_ls2[-1])
    else:
        ss=array(list(s0-s1))
        std_ls2.append(mean(load_sf_stded_over_trial(c,s,tbgn,tend)[ss]))



c=3  # couple
s=0  # shift
std_ls3=[0]
for th in range(sf_min,sf_max):
    s0=set(filter_active_PN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_PN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        std_ls3.append(std_ls3[-1])
    else:
        ss=array(list(s0-s1))
        std_ls3.append(mean(load_sf_stded_over_trial(c,s,tbgn,tend)[ss]))


c=4  # couple
s=0  # shift
std_ls4=[0]
for th in range(sf_min,sf_max):
    s0=set(filter_active_PN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_PN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        std_ls4.append(std_ls4[-1])
    else:
        ss=array(list(s0-s1))
        std_ls4.append(mean(load_sf_stded_over_trial(c,s,tbgn,tend)[ss]))


plot((array(std_ls0[1:])+array(std_ls1[1:])+array(std_ls2[1:])+array(std_ls3[1:])+array(std_ls4[1:]))/5.0)

'''
plot(load_sf_avged_over_trial(0,0,tbgn,tend), load_sf_stded_over_trial(0,0,tbgn,tend), '.', markersize=2) #, color='g')
plot(load_sf_avged_over_trial(1,0,tbgn,tend), load_sf_stded_over_trial(1,0,tbgn,tend), '.', markersize=2) #, color='g')
plot(load_sf_avged_over_trial(2,0,tbgn,tend), load_sf_stded_over_trial(2,0,tbgn,tend), '.', markersize=2) #, color='g')
plot(load_sf_avged_over_trial(3,0,tbgn,tend), load_sf_stded_over_trial(3,0,tbgn,tend), '.', markersize=2) #, color='g')
plot(load_sf_avged_over_trial(4,0,tbgn,tend), load_sf_stded_over_trial(4,0,tbgn,tend), '.', markersize=2) #, color='c')
'''

xlabel("mean fire rate (Hz)")
ylabel("standard deviation")
savefig("sf_std_vs_avg_%d_%d.jpg"%(tbgn,tend))
show()
clf()
