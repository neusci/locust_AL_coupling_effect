#execfile("../slow/slow_analy_head.py")

tbgn=1200
tend=1500 # 3500?
sf_min=5
sf_max=35

print("plot PN number at each firerate")
print("begin time=%d, end time=%d"%(tbgn,tend))


c=0  # couple
s=0  # shift
neurate_ls=[]
for th in range(sf_min,sf_max):
    s0=set(filter_active_NN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_NN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        neurate_ls.append(0)
    else:
        ss=array(list(s0-s1))
        neurate_ls.append(len(ss)*100.0/PN_number)
plot(neurate_ls)


c=1  # couple
s=0  # shift
neurate_ls=[]
for th in range(sf_min,sf_max):
    s0=set(filter_active_NN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_NN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        neurate_ls.append(0)
    else:
        ss=array(list(s0-s1))
        neurate_ls.append(len(ss)*100.0/PN_number)
plot(neurate_ls)


c=2  # couple
s=0  # shift
neurate_ls=[]
for th in range(sf_min,sf_max):
    s0=set(filter_active_NN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_NN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        neurate_ls.append(0)
    else:
        ss=array(list(s0-s1))
        neurate_ls.append(len(ss)*100.0/PN_number)
plot(neurate_ls)


c=3  # couple
s=0  # shift
neurate_ls=[]
for th in range(sf_min,sf_max):
    s0=set(filter_active_NN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_NN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        neurate_ls.append(0)
    else:
        ss=array(list(s0-s1))
        neurate_ls.append(len(ss)*100.0/PN_number)
plot(neurate_ls)


c=4  # couple
s=0  # shift
neurate_ls=[]
for th in range(sf_min,sf_max):
    s0=set(filter_active_NN_from_sf(c,s,tbgn,tend,th-5))
    s1=set(filter_active_NN_from_sf(c,s,tbgn,tend,th))
    if s0==s1:
        neurate_ls.append(0)
    else:
        ss=array(list(s0-s1))
        neurate_ls.append(len(ss)*100.0/PN_number)
plot(neurate_ls)


xlabel('fire rate (Hz)')
ylabel('ratio (%)')
savefig('sf_vs_neuron_ratio_%d_%d.jpg'%(tbgn,tend))
show()
clf()
