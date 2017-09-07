#  !/usr/bin/env python
#  -*- coding:utf-8 -*-
execfile('../slow/slow_analy_head.py')

for c in append(ptCouple_list, 0):
    x_cc_u1 = loadtxt('./data/clss-corr-rate-couple%d-use10PNs.txt'%c)
    x_cc_u2 = loadtxt('./data/clss-corr-rate-couple%d-use20PNs.txt'%c)
    x_cc_u3 = loadtxt('./data/clss-corr-rate-couple%d-use30PNs.txt'%c)
    #x_cc_u4 = loadtxt('./data/clss-corr-rate-couple%d-use40PNs.txt'%c)
    #x_cc_u5 = loadtxt('./data/clss-corr-rate-couple%d-use50PNs.txt'%c)

    x_c100_u1 = loadtxt('./data/clss-corr-rate-couple100-use10PNs.txt')
    x_c100_u2 = loadtxt('./data/clss-corr-rate-couple100-use20PNs.txt')
    x_c100_u3 = loadtxt('./data/clss-corr-rate-couple100-use30PNs.txt')
    #x_c100_u4 = loadtxt('./data/clss-corr-rate-couple100-use40PNs.txt')
    #x_c100_u5 = loadtxt('./data/clss-corr-rate-couple100-use50PNs.txt')

    cc_ls  =[x_cc_u1, x_cc_u2, x_cc_u3] #, x_cc_u4, x_cc_u5]
    c100_ls=[x_c100_u1, x_c100_u2, x_c100_u3] #, x_c100_u4, x_c100_u5]
    avg_cc_ls,   std_cc_ls   = map(avg, cc_ls),   map(std, cc_ls)
    avg_c100_ls, std_c100_ls = map(avg, c100_ls), map(std, c100_ls)

    errorbar(x=range(1,len(cc_ls)+1), y=avg_cc_ls,  yerr=std_cc_ls,  c='purple')
    errorbar(x=range(1,len(c100_ls)+1), y=avg_c100_ls,yerr=std_c100_ls,c='green')
    xlim([0.8,3.2])
    ylim([0.2,1.0])
    xticks([1,2,3], ['10', '20', '30'])
    xlabel('PN number')
    ylabel('correction ratio')
    savefig('./class_corr_ratio_%d.jpg'%c)
    savefig('./class_corr_ratio_%d.eps'%c)
    clf()
