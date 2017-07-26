#execfile("../slow/slow_analy_head.py")

tbgn=analy_time_begin
tend=analy_time_end

print("odor decorr in AL")
print("begin time=%d, end time=%d"%(tbgn,tend))

print("c=100")  #what is this used for?
c=100; s=0; dlsx0=array([comp_distance_from_sf(c,s,0, c,s,t, tbgn,tend)  for t in range(1,5)])

print("c=0")
c=0; s=0; dls00=array([comp_distance_from_sf(c,s,0, c,s,t, tbgn,tend)  for t in range(1,5)])

print("c=1")
c=1; s=0; dls10=array([comp_distance_from_sf(c,s,0, c,s,t, tbgn,tend)  for t in range(1,5)])

print("c=2")
c=2; s=0; dls20=array([comp_distance_from_sf(c,s,0, c,s,t, tbgn,tend)  for t in range(1,5)])

print("c=3")
c=3; s=0; dls30=array([comp_distance_from_sf(c,s,0, c,s,t, tbgn,tend)  for t in range(1,5)])

'''
print("c=4")
c=4; s=0; dls40=array([comp_distance_from_sf(c,s,0, c,s,t, tbgn,tend)  for t in range(1,5)])
plot([mean(dls00), mean(dls10), mean(dls20), mean(dls30), mean(dls40)], '.-');
'''

#dlses=zip([dls00, dls10, dls20, dls30])
print('odor err:', dlsx0)
fill_between(x=range(4), y1=[min(dls00), min(dls10), min(dls20), min(dls30)], y2=[max(dls00), max(dls10), max(dls20), max(dls30)], alpha=0.2, color="#089FFF", antialiased=true)
plot(map(mean, zip([dls00, dls10, dls20, dls30])), '.-', color="m", lw=1.5)
print('repr err:', map(mean, zip([dls00, dls10, dls20, dls30])))

xlabel("tese #")
ylabel("distance")
xticks(range(4))
ylim([100,200])
xlim([-0.1,3.1])
savefig("distance_error_%d_%d.jpg"%(tbgn,tend))
savefig("distance_error_%d_%d.eps"%(tbgn,tend))
show()
