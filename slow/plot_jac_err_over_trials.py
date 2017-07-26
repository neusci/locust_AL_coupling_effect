#execfile("../slow/slow_analy_head.py")

tbgn=analy_time_begin
tend=analy_time_end
s=0  # shift

print("plot diverg of resp sets among trials")
print("begin time=%d, end time=%d"%(tbgn,tend))

def filter_active_PN_on_trial(c,s,t, tbgn,tend, th): return filter_active_PN_from_sf_1trial(c,s,t, tbgn,tend, th)

sdls_c0=[]
sdls_c1=[]
sdls_c2=[]
sdls_c3=[]
#sdls_c4=[]

#==========================================
th=15
c=0  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c0=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c0.append(mean(sd_c0))


c=1  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c1=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c1.append(mean(sd_c1))


c=2  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c2=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c2.append(mean(sd_c2))


c=3  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c3=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c3.append(mean(sd_c3))

'''
c=4  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c4=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c4.append(mean(sd_c4))
'''

#==========================================
th=20
c=0  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c0=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c0.append(mean(sd_c0))


c=1  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c1=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c1.append(mean(sd_c1))


c=2  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c2=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c2.append(mean(sd_c2))


c=3  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c3=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c3.append(mean(sd_c3))

'''
c=4  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c4=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c4.append(mean(sd_c4))
'''

#==========================================
th=25
c=0  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c0=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c0.append(mean(sd_c0))


c=1  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c1=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c1.append(mean(sd_c1))


c=2  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c2=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c2.append(mean(sd_c2))


c=3  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c3=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c3.append(mean(sd_c3))

'''
c=4  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c4=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c4.append(mean(sd_c4))
'''

#==========================================
th=30
c=0  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c0=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c0.append(mean(sd_c0))


c=1  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c1=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c1.append(mean(sd_c1))


c=2  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c2=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c2.append(mean(sd_c2))


c=3  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c3=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c3.append(mean(sd_c3))

'''
c=4  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c4=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c4.append(mean(sd_c4))
'''

#==========================================
th=35
c=0  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c0=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c0.append(mean(sd_c0))


c=1  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c1=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c1.append(mean(sd_c1))


c=2  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c2=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c2.append(mean(sd_c2))


c=3  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c3=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c3.append(mean(sd_c3))

'''
c=4  # couple
s0=set(filter_active_PN_on_trial(c,s,0,tbgn,tend,th))
s1=set(filter_active_PN_on_trial(c,s,1,tbgn,tend,th))
s2=set(filter_active_PN_on_trial(c,s,2,tbgn,tend,th))
s3=set(filter_active_PN_on_trial(c,s,3,tbgn,tend,th))
s4=set(filter_active_PN_on_trial(c,s,4,tbgn,tend,th))
sd_c4=[sets_divergence(s0,s1), sets_divergence(s1,s2), sets_divergence(s2,s3), sets_divergence(s3,s4), sets_divergence(s4,s0)]
sdls_c4.append(mean(sd_c4))
'''

'''
plot(sdls_c0, '.-')
plot(sdls_c1, '.-')
plot(sdls_c2, '.-')
plot(sdls_c3, '.-')
plot(sdls_c4, '.-')
'''

dls0=array(sdls_c0)
dls1=array(sdls_c1)
dls2=array(sdls_c2)
dls3=array(sdls_c3)

dlsAvg=array([mean([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsStd=array([ std([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMax=array([max([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])
dlsMin=array([min([dls0[i], dls1[i], dls2[i], dls3[i] ]) for i in rlen(dls0)])

print(dlsAvg)

fill_between(x=range(5), y1=dlsMin, y2=dlsMax, alpha=0.2, color="#089FFF", antialiased=true)
plot(dlsAvg, '.-', color="m", lw=1.5) #, color='white')

xlabel("threshold (Hz)")
ylabel("diverage between response")
x1 = [0, 1, 2, 3, 4]
labels1 = ['15', '20', '25', '30', '35']
xticks(x1, labels1)
xlim([-0.1, 4.1])
savefig("decorr_error_overtrial_%d_%d.jpg"%(tbgn,tend))
savefig("decorr_error_overtrial_%d_%d.eps"%(tbgn,tend))
show()
clf()
