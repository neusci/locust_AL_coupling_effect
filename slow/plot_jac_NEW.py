#execfile("../slow/slow_analy_head.py")

def enlrg(ls, t):
    # make elems in ls t times larger, and keep them no larger than 1
    nls=array([x*t for x in ls])
    nls[nls>1]=1
    return nls

tbgn=analy_time_begin
tend=analy_time_end
th=PN_resp_thres

# 'errls is obtained by running plot_decorr_error_....py'
errls=array([ 0.4221351 ,  0.39860834,  0.32606195,  0.36776812,  0.64885331])
#               15           20           25           30           35

err=errls[int(round((th-15)/5.0))]

print("odor decorr in AL")
print("begin time=%d, end time=%d, th=%d"%(tbgn,tend,th))
ols=[sets_divergence(odor_IDs(0), odor_IDs(i)) for i in shift_list]  # odor dist list
#ols.append(1)


print("c=0")
c=0; t=0; dls00=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=1; dls01=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=2; dls02=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=3; dls03=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=4; dls04=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

print("c=1")
c=1; t=0; dls10=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=1; dls11=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=2; dls12=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=3; dls13=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=4; dls14=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

print("c=2")
c=2; t=0; dls20=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=1; dls21=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=2; dls22=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=3; dls23=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=4; dls24=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

print("c=3")
c=3; t=0; dls30=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=1; dls31=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=2; dls32=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=3; dls33=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=4; dls34=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

'''
print("c=4")
c=4; t=0; dls40=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=1; dls41=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=2; dls42=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=3; dls43=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=4; dls44=array([comp_sets_diverg_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
'''


dls0=(dls00+dls01+dls02+dls03+dls04)/5.0
dls1=(dls10+dls11+dls12+dls13+dls14)/5.0
dls2=(dls20+dls21+dls22+dls23+dls24)/5.0
dls3=(dls30+dls31+dls32+dls33+dls34)/5.0
#dls4=(dls40+dls41+dls42+dls43+dls44)/5.0

'''
dls0=dls0-dls0[1]+ols[1]
dls1=dls1-dls1[1]+ols[1]
dls2=dls2-dls2[1]+ols[1]
dls3=dls3-dls3[1]+ols[1]
#dls4=dls4-dls4[1]+ols[1]
'''

dls0=dls0-err
dls1=dls1-err
dls2=dls2-err
dls3=dls3-err

dls0[0]=0
dls1[0]=0
dls2[0]=0
dls3[0]=0

dlsAvg=array([mean([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsStd=array([ std([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMin=array([ min([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMax=array([ max([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])

fplot("y=x", [0,1])
fill_between(x=ols, y1=dlsMin, y2=dlsMax, alpha=0.2, color="#089FFF", antialiased=true)
plot(ols, dlsAvg, '.-', color='m'); #white');
print(dlsAvg)

'''
plot(ols, append((dls00+dls01+dls02+dls03+dls04)/5.0, 1), '.-');
plot(ols, append((dls10+dls11+dls12+dls13+dls14)/5.0, 1), '.-');
plot(ols, append((dls20+dls21+dls22+dls23+dls24)/5.0, 1), '.-');
plot(ols, append((dls30+dls31+dls32+dls33+dls34)/5.0, 1), '.-');
plot(ols, append((dls40+dls41+dls42+dls43+dls44)/5.0, 1), '.-');
'''

xlim([0,1])
ylim([0,1])
xlabel("stimulation divergence")
ylabel("representation divergence")
savefig("decorr_NEW_th%d_%d_%d.jpg"%(th,tbgn,tend))
savefig("decorr_NEW_th%d_%d_%d.eps"%(th,tbgn,tend))
show()

stp=8
sls=[]
for i in range(len(ols)-stp):
    x=ols[i:i+stp]
    y=dlsAvg[i:i+stp]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    sls.append(slope)

plot(sls, '.-')
xlabel("#")
ylabel("slope")
savefig("decorr_slope_th%d_%d_%d.jpg"%(th,tbgn,tend))
savefig("decorr_slope_th%d_%d_%d.eps"%(th,tbgn,tend))
show()

tt=1.666667
fplot('y=x', [0,1])
plot(ols, enlrg(dlsAvg, tt))
xlabel('odors')
ylabel('representations')
savefig("sigmoid_th%d_%d_%d_times%d.jpg"%(th,tbgn,tend,tt))
savefig("sigmoid_th%d_%d_%d_times%d.eps"%(th,tbgn,tend,tt))
show()
