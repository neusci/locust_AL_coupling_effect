#execfile("slow_analy_head.py")

tbgn=1100
tend=3500
th=30
delta=1

c=0; s=0
print("plot corr between vol of PNs with fire rate th(th~th+delta) and vol of all PNs")
print("begin time=%d, end time=%d, th=%d, delta=%d"%(tbgn,tend,th,delta))
print("  for couple:%d, shift:%d, the corr_coeff is:"%(c,s))

def osc_of_most_inactive_PNs(c,s,tb,te,th0,th1):
    s0=filter_inactive_NN_from_sf(c,s,tb,te,th0)
    s1=filter_inactive_NN_from_sf(c,s,tb,te,th1)
    if th1>0:ss=set(s1)-set(s0)
    else:ss=s1
    ss=map(int, ss)
    return sum(x[array(ss)], 0)

x=loaddata(c,s,0)[:,tbgn:tend]
# plot(sum(x[filter_inactive_PN_from_sf(0,0,1100,1500,0)], 0)*100+200000); plot(sum(x, 0)); show()
# xxx=sum(x[filter_inactive_PN_from_sf(0,0,1100,1500,0)], 0)*100+200000; yyy=sum(x, 0); plot(xxx,yyy,'.'); show()
xxx=osc_of_most_inactive_PNs(c,s,tbgn,tend,th,th+delta)
yyy=sum(x, 0)
slope, intercept, r_value, p_value, std_err = stats.linregress(xxx, yyy)
print(r_value)
plot(xxx,yyy,'.')
#show()
savefig("inactive_vs_osc_corr_coeff.jpg")
savefig("inactive_vs_osc_corr_coeff.eps")
clf()
