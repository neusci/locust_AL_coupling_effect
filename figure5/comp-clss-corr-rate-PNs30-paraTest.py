execfile('../slow/slow_analy_head.py')


tb = 1100
te = 1350
use_num = 30  #use 20 PNs (of 830 PNs)
print('use %d PNs'%use_num)

try_num = 100 # try 100 times (selsect 100 group PNs)


def dist_to_cent(x, cent_ls):
    # distance from x to each center (each mean)
    return [norm(x-i) for i in cent_ls]

def if_class_corr(x, s, cent_ls):
    # if the nearest neighbor of x is the correct center?:
    #    True  --- correct
    #    False --- wrong
    dist_ls = dist_to_cent(x, cent_ls)
    # dist_ls[s]==min(dist_ls):
    if 0.999 < (1.0*dist_ls[s]/min(dist_ls)) < 1.001:
        #print(dist_ls,s,True)
        return 1 # True
    else:
        #print(dist_ls,s,False)
        return 0 #False


all_coup_ls = append(ptCouple_list, [0,100])
ccr = zeros([len(all_coup_ls),try_num])


for the_ith_try in range(try_num):
    print('\n\ntry:',the_ith_try)
    use_idx = choice(range(PN_number), use_num) # random select the PNs
    print('PNs:', use_idx)
    # ...
    for c in rlen(all_coup_ls):
        coup = all_coup_ls[c]
        corr_num = 0
        total_num = 0
        cent_ls = [load_sf_avged_over_trial(coup,sft,tb,te)[use_idx] for sft in ptShift_list]
        # ...
        for s in range(ptShift_number):  # how many trials of s-th odor(shift) correctly classfied??
            sft = ptShift_list[s]
            # ...
            for t in range(ptTrial_number): # all the shifts and trials are considered..
                total_num += 1
                x = load_sf_from_file(coup,sft,t,tb,te)[use_idx]
                corr_num += if_class_corr(x,s,cent_ls)
        ccr[c, the_ith_try]=1.0*corr_num/total_num
        print('for couple', coup, ', the classify correct ratios:', ccr[c, the_ith_try])


for c in rlen(all_coup_ls):
    coup = all_coup_ls[c]
    savetxt('./data/clss-corr-rate-couple%d-use%dPNs.txt'%(coup, use_num), ccr[c,:])
