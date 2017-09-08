execfile('../slow/slow_analy_head.py')


idx = range(PN_number)
tb = 1100
te = 1350
use_num = 30  #use 30 PNs (of 830 PNs)
print('use %d PNs'%use_num)


def dist_to_cent(x, cent_ls):
    # distance from x to each center (each mean)
    return [norm(x-i) for i in cent_ls]

def if_class_corr(x, s, cent_ls):
    # if the nearest neighbor of x is the correct center?:
    #    True  --- correct
    #    False --- wrong
    dist_ls = dist_to_cent(x, cent_ls)
    s = int(round(s/12)) # this is 12 for paraTest cases
    #if 0.99999<(1.0*dist_ls[s]/min(dist_ls))<1.00001: return 1 # True
    if dist_ls[s]==min(dist_ls):
        return 1
    else:
        return 0 #False


try_num = 50 # try 100 times (selsect 100 group PNs)
resp_ccr = zeros(try_num)
stim_ccr = zeros(try_num)
stim_coup = 100


for the_ith_try in range(try_num):
    print('\n\ntry:',the_ith_try)
    use_idx = choice(idx,use_num) # random select the PNs
    print('PNs:', use_idx)
    # ...
    for resp_coup in append(ptCouple_list, [0,100]):
        resp_cent_ls = [load_sf_avged_over_trial(resp_coup,s,tb,te)[use_idx] for s in ptShift_list]
        resp_corr_num = 0
        resp_total_num = 0
        for s in ptShift_list:  # how many trials of s-th odor(shift) correctly classfied??
            for t in range(ptTrial_number): # all the shifts and trials are considered...
                resp_total_num += 1
                x=load_sf_from_file(resp_coup,s,t,tb,te)[use_idx]
                resp_corr_num += if_class_corr(x,s,resp_cent_ls)
        resp_this_ccr=1.0*resp_corr_num/resp_total_num
        print('for couple', resp_coup, ', the classify correct ratio is:', resp_this_ccr)
        resp_ccr[the_ith_try]=resp_this_ccr
        # ...
        savetxt('./data/clss-corr-rate-couple%d-use%dPNs.txt'%(resp_coup, use_num), resp_ccr)
