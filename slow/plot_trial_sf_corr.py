execfile("slow_analy_head.py")

tbgn=1200
tend=1500
print('plot the corr of each PNs spike freq between trials')
print('     time period', tbgn, tend)

c=0
x0=load_sf_from_file(c,0,0,tbgn,tend)
y0=load_sf_from_file(c,0,1,tbgn,tend)

c=1
x1=load_sf_from_file(c,0,0,tbgn,tend)
y1=load_sf_from_file(c,0,1,tbgn,tend)

c=2
x2=load_sf_from_file(c,0,0,tbgn,tend)
y2=load_sf_from_file(c,0,1,tbgn,tend)

c=3
x3=load_sf_from_file(c,0,0,tbgn,tend)
y3=load_sf_from_file(c,0,1,tbgn,tend)


plot(jittering(x0,1,1), jittering(y0,1,1), '.', ms=2)
plot(jittering(x1,1,1), jittering(y1,1,1), '.', ms=2)
plot(jittering(x2,1,1), jittering(y2,1,1), '.', ms=2)
plot(jittering(x3,1,1), jittering(y3,1,1), '.', ms=2)

savefig("trial_sf_corr_%d_%d.jpg"%(tbgn,tend))
savefig("trial_sf_corr_%d_%d.eps"%(tbgn,tend))
xlim([-5,45])
ylim([-5,45])
show()
clf()
