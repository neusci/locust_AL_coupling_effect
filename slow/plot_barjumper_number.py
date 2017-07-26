execfile("../slow/slow_analy_head.py")

tbgn=1100
tend=3500
th=20
print("plot the number of PNs that jumps over the barrier")
print("begin time=%d, end time=%d, th=%d"%(tbgn,tend,th))

c=0; t=0; dls00=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=1; dls01=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=2; dls02=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=3; dls03=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=0; t=4; dls04=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

c=1; t=0; dls10=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=1; dls11=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=2; dls12=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=3; dls13=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=1; t=4; dls14=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

c=2; t=0; dls20=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=1; dls21=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=2; dls22=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=3; dls23=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=2; t=4; dls24=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

c=3; t=0; dls30=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=1; dls31=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=2; dls32=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=3; dls33=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=3; t=4; dls34=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

c=4; t=0; dls40=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=1; dls41=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=2; dls42=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=3; dls43=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])
c=4; t=4; dls44=array([count_barrier_jumper_from_sf(c,0,t, c,s,t, tbgn,tend, th)  for s in shift_list])

'''
fplot('y=x', [0,80]);
#if th==30: fplot('y=x+5.5', [0,80]);
plot(shift_list, (dls00+dls01+dls02+dls03+dls04)/5.0, '.-');
plot(shift_list, (dls10+dls11+dls12+dls13+dls14)/5.0, '.-');
plot(shift_list, (dls20+dls21+dls22+dls23+dls24)/5.0, '.-');
plot(shift_list, (dls30+dls31+dls32+dls33+dls34)/5.0, '.-');
plot(shift_list, (dls40+dls41+dls42+dls43+dls44)/5.0, '.-');
'''


dls0=(dls00+dls01+dls02+dls03+dls04)/5.0
dls1=(dls10+dls11+dls12+dls13+dls14)/5.0
dls2=(dls20+dls21+dls22+dls23+dls24)/5.0
dls3=(dls30+dls31+dls32+dls33+dls34)/5.0
dls4=(dls40+dls41+dls42+dls43+dls44)/5.0

dls0=dls0-dls0[1]+shift_list[1]
dls1=dls1-dls1[1]+shift_list[1]
dls2=dls2-dls2[1]+shift_list[1]
dls3=dls3-dls3[1]+shift_list[1]
dls4=dls4-dls4[1]+shift_list[1]

dlsAvg=array([mean([dls0[i], dls1[i], dls2[i], dls3[i], dls4[i] ]) for i in rlen(dls0)])
dlsStd=array([ std([dls0[i], dls1[i], dls2[i], dls3[i], dls4[i] ]) for i in rlen(dls0)])

fill_between(x=shift_list, y1=(dlsAvg-2*dlsStd), y2=(dlsAvg+2*dlsStd), alpha=0.2, color="#089FFF", antialiased=true)
plot(shift_list[1:], dlsAvg[1:], '.-', color='white');


xlabel("shifted stim PN number")
ylabel("shifted resp PN number")
xlim([0,81]);
savefig("barjumper_number_th%d_%d_%d.jpg"%(th,tbgn,tend))
show()


sls=[]
for i in range(len(ols)-4):
    x=ols[i:i+4]
    y=dlsAvg[i:i+4]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    sls.append(slope)

plot(sls[1:])
savefig("barjumper_slope_th%d_%d_%d.jpg"%(th,tbgn,tend))
show()
