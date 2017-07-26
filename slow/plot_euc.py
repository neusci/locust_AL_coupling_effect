#execfile("../slow/slow_analy_head.py")

tbgn=analy_time_begin
tend=analy_time_end
# 'errls is obtained by running plot_distance_error_....py'
#errls=[171.41601248301976, 178.29603154600534, 173.64561776036172, 167.96717662798812]

print("odor decorr in AL")
print("begin time=%d, end time=%d"%(tbgn,tend))


#ols=[norm(generate_odor_sf(odor_IDs(0))-generate_odor_sf(odor_IDs(i))) for i in shift_list]  # odor dist list
c=100; t=0; dlsx0=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=1; dlsx1=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=2; dlsx2=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=3; dlsx3=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=100; t=4; dlsx4=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

#ols=(dlsx0+dlsx1+dlsx2+dlsx3+dlsx4)/5.0-63.338674  # the Euc error 63.x can be computed in the same as the others
#ols[0] = 0
ols=(dlsx0+dlsx1+dlsx2+dlsx3+dlsx4)/5.0   #  use this line if error no substracting...

print("c=0")
c=0; t=0; dls00=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=1; dls01=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=2; dls02=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=3; dls03=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=0; t=4; dls04=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

print("c=1")
c=1; t=0; dls10=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=1; dls11=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=2; dls12=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=3; dls13=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=1; t=4; dls14=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

print("c=2")
c=2; t=0; dls20=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=1; dls21=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=2; dls22=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=3; dls23=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=2; t=4; dls24=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

print("c=3")
c=3; t=0; dls30=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=1; dls31=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=2; dls32=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=3; dls33=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=3; t=4; dls34=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])

'''
print("c=4")
c=4; t=0; dls40=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=4; t=1; dls41=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=4; t=2; dls42=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=4; t=3; dls43=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
c=4; t=4; dls44=array([comp_distance_from_sf(c,0,t, c,s,t, tbgn,tend)  for s in shift_list])
'''

dls0=(dls00+dls01+dls02+dls03+dls04)/5.0
dls1=(dls10+dls11+dls12+dls13+dls14)/5.0
dls2=(dls20+dls21+dls22+dls23+dls24)/5.0
dls3=(dls30+dls31+dls32+dls33+dls34)/5.0
#dls4=(dls40+dls41+dls42+dls43+dls44)/5.0

''' # comment these 2 paragraphes when the error is not substracted
dls0=dls0-errls[0]
dls1=dls1-errls[1]
dls2=dls2-errls[2]
dls3=dls3-errls[3]
#dls4=dls4-dls4[1]+ols[1]

dls0[0]=0
dls1[0]=0
dls2[0]=0
dls3[0]=0
#dls4[0]=0
'''

#dlsAvg=array([mean([dls0[i], dls1[i], dls2[i], dls3[i], dls4[i] ]) for i in rlen(dls0)])
#dlsStd=array([ std([dls0[i], dls1[i], dls2[i], dls3[i], dls4[i] ]) for i in rlen(dls0)])

dlsAvg=array([mean([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsStd=array([ std([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMax=array([ max([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMin=array([ min([ dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])

'''
plot(ols, (dls00+dls01+dls02+dls03+dls04)/5.0, '.-');
plot(ols, (dls10+dls11+dls12+dls13+dls14)/5.0, '.-');
plot(ols, (dls20+dls21+dls22+dls23+dls24)/5.0, '.-');
plot(ols, (dls30+dls31+dls32+dls33+dls34)/5.0, '.-');
plot(ols, (dls40+dls41+dls42+dls43+dls44)/5.0, '.-');
'''

fplot("y=x", [0,500])

fill_between(x=ols, y1=dlsMin, y2=dlsMax, alpha=0.2, color="#089FFF", antialiased=true)
#fill_between(x=ols, y1=(dlsAvg-2*dlsStd), y2=(dlsAvg+2*dlsStd), alpha=0.2, color="#089FFF", antialiased=true)
##plot(ols[1:], dlsAvg[1:], '.-', color='white');
plot(ols, dlsAvg, '.-', color='m'); #white');

#xlim([0,400])
#ylim([0,400])
xlabel("stimulation distance")
ylabel("representation distance")
savefig("distance_%d_%d.jpg"%(tbgn,tend))
savefig("distance_%d_%d.eps"%(tbgn,tend))
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

savefig("distance_slope_%d_%d.jpg"%(tbgn,tend))
savefig("distance_slope_%d_%d.eps"%(tbgn,tend))
show()
clf()
