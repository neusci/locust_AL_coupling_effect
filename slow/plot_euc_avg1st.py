#execfile("../slow/slow_analy_head.py")

tbgn=analy_time_begin
tend=analy_time_end
# 'errls is obtained by running plot_distance_error_....py'
#errls=[171.41601248301976, 178.29603154600534, 173.64561776036172, 167.96717662798812]

print("odor decorr in AL")
print("begin time=%d, end time=%d"%(tbgn,tend))

c=100; osfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=0;   asfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=1;   bsfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=2;   csfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=3;   dsfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])


ols=array([norm(x-osfls[0]) for x in osfls])
als=array([norm(x-asfls[0]) for x in asfls])
bls=array([norm(x-bsfls[0]) for x in bsfls])
cls=array([norm(x-csfls[0]) for x in csfls])
dls=array([norm(x-dsfls[0]) for x in dsfls])

rls=(als+bls+cls+dls)/4.0
rMin=[min(als[i],bls[i],cls[i],dls[i]) for i in rlen(ols)]
rMax=[max(als[i],bls[i],cls[i],dls[i]) for i in rlen(ols)]

fill_between(x=ols, y1=rMin, y2=rMax, alpha=0.2, color="#089FFF", antialiased=true)
plot(ols, rls, '.-', color='m'); #white');
print('odor ls: ', ols)
print('repr ls: ', rls)

fplot("y=x", [0,500])
plot(ols, rls, '.-', color='m'); #white');

#xlim([0,400])
#ylim([0,400])
xlabel("stimulation distance")
ylabel("representation distance")
savefig("distance_%d_%d_avg1st-withFast.jpg"%(tbgn,tend))
savefig("distance_%d_%d_avg1st-withFast.eps"%(tbgn,tend))
show()
clf()


stp=4
sls=[]
for i in range(len(ols)-stp):
    x=ols[i:i+stp]
    y=rls[i:i+stp]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    sls.append(slope)

xlabel("#")
ylabel("slope")

plot(sls, '.-')
savefig("distance_slope_%d_%d_avg1st-withFast.jpg"%(tbgn,tend))
savefig("distance_slope_%d_%d_avg1st-withFast.eps"%(tbgn,tend))
show()
clf()
