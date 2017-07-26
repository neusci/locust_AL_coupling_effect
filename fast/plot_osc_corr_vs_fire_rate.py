#execfile("../slow/slow_analy_head.py")
#execfile("../fast/fast_analy_head.py")

tbgn=1200
tend=1500

print("corr of each PN's (1) fire rate and ")
print("     (2) the corr_coeff between the vol of this PN and all PNs")
print("begin time=%d, end time=%d"%(tbgn,tend))


c=0
print(c)
x=load_sf_avged_over_trial(c,0,tbgn,tend)
y0=corr_coeff_array_from_vol_matrix(loaddata(c,0,0), tbgn, tend)
y1=corr_coeff_array_from_vol_matrix(loaddata(c,0,1), tbgn, tend)
y2=corr_coeff_array_from_vol_matrix(loaddata(c,0,2), tbgn, tend)
y3=corr_coeff_array_from_vol_matrix(loaddata(c,0,3), tbgn, tend)
y4=corr_coeff_array_from_vol_matrix(loaddata(c,0,4), tbgn, tend)
plot(jittering(x,0.3,1), jittering(map(abs, (y0+y1+y2+y3+y4)/5.0),0.01,1), '.', markersize=2)


c=1
print(c)
x=load_sf_avged_over_trial(c,0,tbgn,tend)
y0=corr_coeff_array_from_vol_matrix(loaddata(c,0,0), tbgn, tend)
y1=corr_coeff_array_from_vol_matrix(loaddata(c,0,1), tbgn, tend)
y2=corr_coeff_array_from_vol_matrix(loaddata(c,0,2), tbgn, tend)
y3=corr_coeff_array_from_vol_matrix(loaddata(c,0,3), tbgn, tend)
y4=corr_coeff_array_from_vol_matrix(loaddata(c,0,4), tbgn, tend)
plot(jittering(x,0.3,1), jittering(map(abs, (y0+y1+y2+y3+y4)/5.0),0.01,1), '.', markersize=2)

c=2
print(c)
x=load_sf_avged_over_trial(c,0,tbgn,tend)
y0=corr_coeff_array_from_vol_matrix(loaddata(c,0,0), tbgn, tend)
y1=corr_coeff_array_from_vol_matrix(loaddata(c,0,1), tbgn, tend)
y2=corr_coeff_array_from_vol_matrix(loaddata(c,0,2), tbgn, tend)
y3=corr_coeff_array_from_vol_matrix(loaddata(c,0,3), tbgn, tend)
y4=corr_coeff_array_from_vol_matrix(loaddata(c,0,4), tbgn, tend)
plot(jittering(x,0.3,1), jittering(map(abs, (y0+y1+y2+y3+y4)/5.0),0.01,1), '.', markersize=2)


c=3
print(c)
x=load_sf_avged_over_trial(c,0,tbgn,tend)
y0=corr_coeff_array_from_vol_matrix(loaddata(c,0,0), tbgn, tend)
y1=corr_coeff_array_from_vol_matrix(loaddata(c,0,1), tbgn, tend)
y2=corr_coeff_array_from_vol_matrix(loaddata(c,0,2), tbgn, tend)
y3=corr_coeff_array_from_vol_matrix(loaddata(c,0,3), tbgn, tend)
y4=corr_coeff_array_from_vol_matrix(loaddata(c,0,4), tbgn, tend)
plot(jittering(x,0.3,1), jittering(map(abs, (y0+y1+y2+y3+y4)/5.0),0.01,1), '.', markersize=2)

'''
c=4
print(c)
x=load_sf_avged_over_trial(c,0,tbgn,tend)
y0=corr_coeff_array_from_vol_matrix(loaddata(c,0,0), tbgn, tend)
y1=corr_coeff_array_from_vol_matrix(loaddata(c,0,1), tbgn, tend)
y2=corr_coeff_array_from_vol_matrix(loaddata(c,0,2), tbgn, tend)
y3=corr_coeff_array_from_vol_matrix(loaddata(c,0,3), tbgn, tend)
y4=corr_coeff_array_from_vol_matrix(loaddata(c,0,4), tbgn, tend)
plot(jittering(x,0.3,1), jittering(map(abs, (y0+y1+y2+y3+y4)/5.0),1,1), '.')
plot(x,map(abs, (y0+y1+y2+y3+y4)/5.0),'.')
'''

xlim([-1,40])
ylim([-0.02,0.8])
xlabel("fire rate (Hz)")
ylabel("correlation with oscillation")
savefig("osc_corr_vs_fire_rate_%d_%d.jpg"%(tbgn,tend))
savefig("osc_corr_vs_fire_rate_%d_%d.eps"%(tbgn,tend))
show()
clf()
