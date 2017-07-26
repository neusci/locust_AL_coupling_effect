execfile("../slow/slow_analy_head.py")
# execfile("../fast/fast_analy_head.py")
# do this manually..

tbgn = 1000
tend = 2000 # real_end?
tlen = 1.0*(tend-tbgn) # tlen:  3500
plen = 100 # 50,100,200,500
nprd = int(floor(1.0*tlen/plen)) # ignore the last region...
p_ls=[ [tbgn+round(i*plen), tbgn+round((i+1)*plen)] for i in range(nprd)]

print("Plot ppcc from each shift to shift0")
print("time period list:", p_ls)

def get_an_odor_resp(c,tb,te,cd=50):
    asf_trial_ls = array([[load_spec_sf_1trial(c,s,t,tb,te,cd) \
                           for t in range(trial_number)] for s in shift_list])
    # In [10]: shape(asf_trial_ls)
    # Out[10]: (25, 10, 830)
    #           25 shifts for the given couple,
    #           10 trials for each shift, and
    #           830 PNs for each trial...
    # ...
    dis_trial_ls = zeros([shift_number, trial_number])
    asf_ref = 1.0*sum(asf_trial_ls[0],0)/trial_number
    # ...
    for i in range(shift_number):
        for j in range(trial_number):
            dis_trial_ls[i,j] = corrcoef([asf_trial_ls[i,j],asf_ref])[0,1]
    # ...
    dis_avg_ls=[avg(x) for x in dis_trial_ls]
    dis_std_ls=[std(x) for x in dis_trial_ls]
    return dis_avg_ls, dis_std_ls, dis_trial_ls

for tb,te in p_ls: #[[1100,1300]]
    print(tb, datetime_str())
    odor_avg, odor_std, _ = get_an_odor_resp(odor_coupling, tb, te)
    resp_avg_ls, resp_std_ls = [], []

    for c in range(couple_number):
        respA,respD,_=get_an_odor_resp(c, tb, te)
        resp_avg_ls.append(respA)
        resp_std_ls.append(respD)

    resp_avg_ls, resp_std_ls = array(resp_avg_ls), array(resp_std_ls)
    resp_avg = 1.0*sum(resp_avg_ls,0)/couple_number
    resp_std = 1.0*sum(resp_std_ls,0)/couple_number
    fill_between(x=odor_avg, y1=resp_avg-resp_std, y2=resp_avg+resp_std, \
                 alpha=0.2, color="#089FFF", antialiased=true)
    plot(odor_avg, resp_avg, '.-', color='white');

fig_len=1
fplot("y=x", [0,fig_len])
xlim([0,fig_len])
ylim([0,fig_len])
xlabel("stimulation ppcc")
ylabel("representation ppcc")
savefig("ppcc_%d_%d_%d.jpg"%(tbgn,tend,plen))
savefig("ppcc_%d_%d_%d.eps"%(tbgn,tend,plen))
clf()
