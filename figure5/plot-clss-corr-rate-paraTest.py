#  !/usr/bin/env python
execfile('../slow/slow_analy_head.py')

tb = 1100
te = 1350


if tb == 1100 and te == 1350:
    x_c100_u1 = loadtxt('./data/clss-corr-rate-couple100-use10PNs.txt')
    x_c100_u2 = loadtxt('./data/clss-corr-rate-couple100-use20PNs.txt')
    x_c100_u3 = loadtxt('./data/clss-corr-rate-couple100-use30PNs.txt')
    x_c100_u4 = loadtxt('./data/clss-corr-rate-couple100-use40PNs.txt')
    x_c100_u5 = loadtxt('./data/clss-corr-rate-couple100-use50PNs.txt')
elif tb == 1050 and te == 1300:
    x_c100_u1 = loadtxt('./data/clss-corr-rate-couple100-use10PNs-2.txt')
    x_c100_u2 = loadtxt('./data/clss-corr-rate-couple100-use20PNs-2.txt')
    x_c100_u3 = loadtxt('./data/clss-corr-rate-couple100-use30PNs-2.txt')
    x_c100_u4 = loadtxt('./data/clss-corr-rate-couple100-use40PNs-2.txt')
    x_c100_u5 = loadtxt('./data/clss-corr-rate-couple100-use50PNs-2.txt')
else:
    x_c100_u1 = loadtxt('./data/clss-corr-rate-couple100-use10PNs-3.txt')
    x_c100_u2 = loadtxt('./data/clss-corr-rate-couple100-use20PNs-3.txt')
    x_c100_u3 = loadtxt('./data/clss-corr-rate-couple100-use30PNs-3.txt')
    x_c100_u4 = loadtxt('./data/clss-corr-rate-couple100-use40PNs-3.txt')
    x_c100_u5 = loadtxt('./data/clss-corr-rate-couple100-use50PNs-3.txt')

c100_ls=[x_c100_u1, x_c100_u2, x_c100_u3, x_c100_u4, x_c100_u5]
avg_c100_ls, std_c100_ls = map(avg, c100_ls), map(std, c100_ls)
errorbar(x=range(1,len(c100_ls)+1), y=avg_c100_ls, yerr=std_c100_ls,
         c=color_ofc(100), label=label_ofc(100,'GABA')) # GABA or couple?!

for c in ptCouple_list:
    if tb == 1100 and te == 1350:
        x_cc_u1 = loadtxt('./data/clss-corr-rate-couple%d-use10PNs.txt'%c)
        x_cc_u2 = loadtxt('./data/clss-corr-rate-couple%d-use20PNs.txt'%c)
        x_cc_u3 = loadtxt('./data/clss-corr-rate-couple%d-use30PNs.txt'%c)
        x_cc_u4 = loadtxt('./data/clss-corr-rate-couple%d-use40PNs.txt'%c)
        x_cc_u5 = loadtxt('./data/clss-corr-rate-couple%d-use50PNs.txt'%c)
    elif tb == 1050 and te == 1300:
        x_cc_u1 = loadtxt('./data/clss-corr-rate-couple%d-use10PNs-2.txt'%c)
        x_cc_u2 = loadtxt('./data/clss-corr-rate-couple%d-use20PNs-2.txt'%c)
        x_cc_u3 = loadtxt('./data/clss-corr-rate-couple%d-use30PNs-2.txt'%c)
        x_cc_u4 = loadtxt('./data/clss-corr-rate-couple%d-use40PNs-2.txt'%c)
        x_cc_u5 = loadtxt('./data/clss-corr-rate-couple%d-use50PNs-2.txt'%c)
    else:
        x_cc_u1 = loadtxt('./data/clss-corr-rate-couple%d-use10PNs-3.txt'%c)
        x_cc_u2 = loadtxt('./data/clss-corr-rate-couple%d-use20PNs-3.txt'%c)
        x_cc_u3 = loadtxt('./data/clss-corr-rate-couple%d-use30PNs-3.txt'%c)
        x_cc_u4 = loadtxt('./data/clss-corr-rate-couple%d-use40PNs-3.txt'%c)
        x_cc_u5 = loadtxt('./data/clss-corr-rate-couple%d-use50PNs-3.txt'%c)

    cc_ls  =[x_cc_u1, x_cc_u2, x_cc_u3, x_cc_u4, x_cc_u5]
    avg_cc_ls, std_cc_ls = map(avg, cc_ls), map(std, cc_ls)
    errorbar(x=range(1,len(cc_ls)+1), y=avg_cc_ls, yerr=std_cc_ls,
             c=color_ofc(c), label=label_ofc(c,'GABA'))
                             # GABA or couple, be careful!!

legend()
xlim([0.8,5.2])
ylim([0.2,1.0])
xticks([1,2,3,4,5], ['10', '20', '30', '40', '50'])
xlabel('PN number')
ylabel('correction ratio')
# ...
if tb == 1100 and te == 1350:
    savefig('./class_corr_ratio_paraTest.jpg')
    savefig('./class_corr_ratio_paraTest.eps')
elif tb == 1050 and te == 1300:
    savefig('./class_corr_ratio_paraTest-2.jpg')
    savefig('./class_corr_ratio_paraTest-2.eps')
else:
    savefig('./class_corr_ratio_paraTest-3.jpg')
    savefig('./class_corr_ratio_paraTest-3.eps')
# ...
clf()
