#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

x_c0_u1 = loadtxt('./data/clss-corr-rate-couple0-use10PNs.txt')
x_c0_u2 = loadtxt('./data/clss-corr-rate-couple0-use20PNs.txt')
x_c0_u3 = loadtxt('./data/clss-corr-rate-couple0-use30PNs.txt')
x_c0_u4 = loadtxt('./data/clss-corr-rate-couple0-use40PNs.txt')
x_c0_u5 = loadtxt('./data/clss-corr-rate-couple0-use50PNs.txt')

x_c100_u1 = loadtxt('./data/clss-corr-rate-couple100-use10PNs.txt')
x_c100_u2 = loadtxt('./data/clss-corr-rate-couple100-use20PNs.txt')
x_c100_u3 = loadtxt('./data/clss-corr-rate-couple100-use30PNs.txt')
x_c100_u4 = loadtxt('./data/clss-corr-rate-couple100-use40PNs.txt')
x_c100_u5 = loadtxt('./data/clss-corr-rate-couple100-use50PNs.txt')

avg_c0_ls = map(avg, [x_c0_u1, x_c0_u2, x_c0_u3, x_c0_u4, x_c0_u5])
avg_c100_ls = map(avg, [x_c100_u1, x_c100_u2, x_c100_u3, x_c100_u4, x_c100_u5])

plot(range(1,6), avg_c0_ls, '.-')
plot(range(1,6), avg_c100_ls, 'x-')
xlim([0.8,5.2])
ylim([0.2,1.0])
xticks([1,2,3,4,5], ['10', '20', '30', '40', '50'])
xlabel('PN number')
ylabel('correction ratio')
savefig('./class_corr_ratio.jpg')
savefig('./class_corr_ratio.eps')
show()
