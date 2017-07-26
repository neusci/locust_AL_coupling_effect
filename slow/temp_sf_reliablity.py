execfile("import_all.py")


a1 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1000_1050.txt")+randn(PN_number)
a2 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1050_1100.txt")+randn(PN_number)
a3 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1100_1150.txt")+randn(PN_number)
a4 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1150_1200.txt")+randn(PN_number)
a5 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1200_1250.txt")+randn(PN_number)
a6 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1250_1300.txt")+randn(PN_number)
a7 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1300_1350.txt")+randn(PN_number)
a8 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1350_1400.txt")+randn(PN_number)
a9 = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1400_1450.txt")+randn(PN_number)
aA = loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq_1450_1500.txt")+randn(PN_number)

b1 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1000_1050.txt")+randn(PN_number)
b2 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1050_1100.txt")+randn(PN_number)
b3 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1100_1150.txt")+randn(PN_number)
b4 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1150_1200.txt")+randn(PN_number)
b5 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1200_1250.txt")+randn(PN_number)
b6 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1250_1300.txt")+randn(PN_number)
b7 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1300_1350.txt")+randn(PN_number)
b8 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1350_1400.txt")+randn(PN_number)
b9 = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1400_1450.txt")+randn(PN_number)
bA = loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq_1450_1500.txt")+randn(PN_number)


x=(a3+a4+a5+a6+b3+b4+b5+b6)/8.0
y=(a7+a8+a9+aA+b7+b8+b9+bA)/8.0
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plot(x, y, '.')
title(r_value)
show()


x=(a2+a3+a4+a5+a6+a7+a8+a9+aA)/9.0
y=(b2+b3+b4+b5+b6+b7+b8+b9+bA)/9.0
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plot(x, y, '.')
title(r_value)
show()


x=loadtxt(cst_to_dir(0,0,0)+"PN_spike_freq.txt")[:,1]
y=loadtxt(cst_to_dir(0,0,1)+"PN_spike_freq.txt")[:,1]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plot(x, y, '.')
title(r_value)
show()
