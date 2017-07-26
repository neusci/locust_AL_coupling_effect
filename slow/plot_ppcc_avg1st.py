#execfile("../slow/slow_analy_head.py")

tbgn=analy_time_begin
tend=analy_time_end

print("compute Pearson product-moment correlation coefficient in AL")
print("begin time=%d, end time=%d"%(tbgn,tend))


def get_corr_coeff(a,b):
    slope, intercept, r_value, p_value, std_err = stats.linregress(a, b)
    return r_value


def comp_ppcc_from_sf(c0,s0,t0, c1,s1,t1, tb,te):
    aaa=load_sf_from_file(c0,s0,t0, tb,te)
    bbb=load_sf_from_file(c1,s1,t1, tb,te)
    return get_corr_coeff(aaa, bbb)


c=100; osfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=0;   asfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=1;   bsfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=2;   csfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])
c=3;   dsfls=array([load_sf_avged_over_trial(c,s,tbgn,tend) for s in shift_list])


ols=array([get_corr_coeff(x, osfls[0]) for x in osfls])
als=array([get_corr_coeff(x, asfls[0]) for x in asfls])
bls=array([get_corr_coeff(x, bsfls[0]) for x in bsfls])
cls=array([get_corr_coeff(x, csfls[0]) for x in csfls])
dls=array([get_corr_coeff(x, dsfls[0]) for x in dsfls])

rls=(als+bls+cls+dls)/4.0
rMin=[min(als[i],bls[i],cls[i],dls[i]) for i in rlen(ols)]
rMax=[max(als[i],bls[i],cls[i],dls[i]) for i in rlen(ols)]

fill_between(x=ols, y1=rMin, y2=rMax, alpha=0.2, color="#089FFF", antialiased=true)
plot(ols, rls, '.-', color='m'); #white');
print(rls)

fplot("y=x", [0,1])

xlabel("stim. corr. coeff.")
ylabel("repr. corr. coeff.")
savefig("ppcc_%d_%d_avg1st.jpg"%(tbgn,tend))
savefig("ppcc_%d_%d_avg1st.eps"%(tbgn,tend))
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
savefig("ppcc_slope_%d_%d_avg1st.jpg"%(tbgn,tend))
savefig("ppcc_slope_%d_%d_avg1st.eps"%(tbgn,tend))
show()
clf()
