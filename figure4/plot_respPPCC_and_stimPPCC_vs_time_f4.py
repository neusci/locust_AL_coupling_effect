execfile("../slow/slow_analy_head.py")
print('copied from ../prime/plot_ppcc_inc.py')

tbgn = real_begin #1100
tend = real_end   #1350
tlen = 1.0*(tend-tbgn)
plen = 50 # 50,100,200,500
nprd = int(floor(1.0*tlen/plen)) # ignore the last region...
p_ls=[ [tbgn+round(i*plen), tbgn+round((i+1)*plen)] for i in range(nprd)]
cList=[0]

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
    ppcc_trial_ls = zeros([shift_number, trial_number])
    asf_ref = 1.0*sum(asf_trial_ls[0],0)/trial_number
    # ...
    for i in range(shift_number):
        for j in range(trial_number):
            ppcc_trial_ls[i,j] = corr(asf_trial_ls[i,j], asf_ref)
    # ...
    ppcc_avg_ls=[avg(x) for x in ppcc_trial_ls]
    ppcc_std_ls=[std(x) for x in ppcc_trial_ls]
    return ppcc_avg_ls, ppcc_std_ls, ppcc_trial_ls

respLs=[]
stimLs=[]

for tb,te in p_ls: #[[1100,1300]]
    print(tb, datetime_str())
    odor_avg, odor_std, _ = get_an_odor_resp(odor_coupling, tb, te)
    resp_avg_ls, resp_std_ls = [], []

    for c in cList:
        respA,respD,_=get_an_odor_resp(c, tb, te)
        resp_avg_ls.append(respA)
        #resp_std_ls.append(respD)

    resp_avg_ls, resp_std_ls = array(resp_avg_ls), array(resp_std_ls)
    resp_avg = 1.0*sum(resp_avg_ls,0)/couple_number
    #resp_std = 1.0*sum(resp_std_ls,0)/couple_number
    stimLs.append(avg(odor_avg))
    respLs.append(avg(resp_avg))

savetxt('./data/stimLS_%d_%d_%d.txt'%(tbgn,tend,plen), stimLs)
savetxt('./data/respLS_%d_%d_%d.txt'%(tbgn,tend,plen), respLs)

plot(stimLs, '.-')
plot(respLs, 'x-')
axvspan(22, 27, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
x1 = [0, 40, 80, 120]
labels1 = ['0', '2000', '4000', '6000']
xticks(x1, labels1)  #, rotation='vertical')

xlabel("time (ms)")
ylabel("stimulation and representation corr coef")
savefig("stim_and_resp_ppcc_vs_time%d_%d_%d.jpg"%(tbgn,tend,plen))
savefig("stim_and_resp_ppcc_vs_time%d_%d_%d.eps"%(tbgn,tend,plen))
show()
clf()

#'''
plot(stimLs[20:40], '.-')
plot(respLs[20:40], 'x-')
axvspan(2, 7, facecolor='0.5', alpha=0.5) # 21-27:50-350ms => 100-400ms
x1 = [0, 5, 10, 15, 20] # plot 1 second
labels1 = ['0', '250', '500', '750', '1000']
xticks(x1, labels1)  #, rotation='vertical')

xlabel("time (ms)")
ylabel("stimulation and representation corr coef")
savefig("stim_and_resp_ppcc_vs_time_fromOnset_%d_%d_%d.jpg"%(0,1000,plen))
savefig("stim_and_resp_ppcc_vs_time_fromOnset_%d_%d_%d.eps"%(0,1000,plen))
show()
clf()
#'''
