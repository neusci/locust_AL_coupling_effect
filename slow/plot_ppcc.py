#execfile("../slow/slow_analy_head.py")

tbgn=analy_time_begin
tend=analy_time_end
th=PN_resp_thres
# 'errls is obtained by running plot_ppcc_error_....py'
##errls = array([ 0.1762971 ,  0.19344256,  0.17506116,  0.16300217]) # for [1200,1500]
#errls = array([ 0.05830918,  0.05921466,  0.05808023,  0.0538065 ]) # for [2000,3000]

print("compute Pearson product-moment correlation coefficient in AL")
print("begin time=%d, end time=%d"%(tbgn,tend))

'''
ols=[]
for i in shift_list:
    slope, intercept, r_value, p_value, std_err = stats.linregress(load_odor_sf(0,cf=tbgn,ct=tend), load_odor_sf(i,cf=tbgn,ct=tend))
    ols.append(r_value)
'''

def comp_ppcc_from_sf(c0,s0,t0, c1,s1,t1, tb,te):
    aaa=load_sf_from_file(c0,s0,t0, tb,te)
    bbb=load_sf_from_file(c1,s1,t1, tb,te)
    slope, intercept, r_value, p_value, std_err = stats.linregress(aaa, bbb)
    return r_value

print("c=0")
c=0; t=0; dls00=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=1; dls01=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=2; dls02=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=3; dls03=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=4; dls04=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

print("c=1")
c=1; t=0; dls10=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=1; dls11=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=2; dls12=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=3; dls13=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=4; dls14=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

print("c=2")
c=2; t=0; dls20=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=1; dls21=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=2; dls22=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=3; dls23=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=4; dls24=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

print("c=3")
c=3; t=0; dls30=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=1; dls31=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=2; dls32=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=3; dls33=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=4; dls34=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

print("c=100")
c=100; t=0; ols0=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=1; ols1=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=2; ols2=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=3; ols3=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=4; ols4=array([comp_ppcc_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

dls0=(dls00+dls01+dls02+dls03+dls04)/5.0
dls1=(dls10+dls11+dls12+dls13+dls14)/5.0
dls2=(dls20+dls21+dls22+dls23+dls24)/5.0
dls3=(dls30+dls31+dls32+dls33+dls34)/5.0
ols =(ols0+ols1+ols2+ols3+ols4)/5.0

'''
dls0=dls0+errls[0]
dls1=dls1+errls[1]
dls2=dls2+errls[2]
dls3=dls3+errls[3]
#dls4=dls4-dls4[1]+ols[1]

dls0[0]=1
dls1[0]=1
dls2[0]=1
dls3[0]=1
'''

#dlsAvg=array([mean([dls0[i], dls1[i], dls2[i], dls3[i], dls4[i] ]) for i in rlen(dls0)])
#dlsStd=array([ std([dls0[i], dls1[i], dls2[i], dls3[i], dls4[i] ]) for i in rlen(dls0)])

dlsAvg=array([mean([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsStd=array([ std([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMax=array([ max([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMin=array([ min([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])

'''
fill_between(x=range(len(dlsAvg)), y1=dlsMin, y2=dlsMax, alpha=0.2, color="#089FFF", antialiased=true)
plot(ols,    '.--', color='r'); #white');
plot(dlsAvg, '*-',  color='m'); #white');
''' # which is better? above or below???
fplot("y=x", [-0.2,1])
fill_between(x=ols, y1=dlsMin, y2=dlsMax, alpha=0.2, color="#089FFF", antialiased=true)
plot(ols, dlsAvg, '.-', color='m'); #white');
print(dlsAvg)

#xlim([-1,1])
#ylim([-1,1])
xlabel("stim. corr. coeff.")
ylabel("repr. corr. coeff.")
savefig("ppcc_%d_%d.jpg"%(tbgn,tend))
savefig("ppcc_%d_%d.eps"%(tbgn,tend))
show()
clf()

stp=4
sls=[]
for i in range(len(ols)-stp):
    x=ols[i:i+stp]
    y=dlsAvg[i:i+stp]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    sls.append(slope)

xlabel("#")
ylabel("slope")

plot(sls, '.-')
# x,y0,y1,y2,y3=diff(ols), diff(dls0), diff(dls1), diff(dls2), diff(dls3)
# plot((y0+y1+y2+y3)/(4.0*x), '.-')

savefig("ppcc_slope_%d_%d.jpg"%(tbgn,tend))
savefig("ppcc_slope_%d_%d.eps"%(tbgn,tend))
show()
clf()
