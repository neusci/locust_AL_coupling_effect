execfile("slow_analy_head.py")

tbgn=1100
tend=3500
s=0
print("plot number of bar-jumper among trials")
print("begin time=%d, end time=%d"%(tbgn,tend))

dls0=[]
dls1=[]
dls2=[]
dls3=[]
dls4=[]

th=15
c=0; dls0.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=1; dls1.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=2; dls2.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=3; dls3.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=4; dls4.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))

th=20
c=0; dls0.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=1; dls1.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=2; dls2.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=3; dls3.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=4; dls4.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))

th=25
c=0; dls0.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=1; dls1.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=2; dls2.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=3; dls3.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=4; dls4.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))

th=30
c=0; dls0.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=1; dls1.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=2; dls2.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=3; dls3.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=4; dls4.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))

th=35
c=0; dls0.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=1; dls1.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=2; dls2.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=3; dls3.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))
c=4; dls4.append(mean([count_barrier_jumper_from_sf(c,s,0, c,s,t, tbgn,tend, th)  for t in range(1,5)]))

'''
plot(dls0, '.-')
plot(dls1, '.-')
plot(dls2, '.-')
plot(dls3, '.-')
plot(dls4, '.-')
'''

plot((array(dls0)+array(dls1)+array(dls2)+array(dls3)+array(dls4))/5.0, '.-')

x1 = [0, 1, 2, 3, 4]
labels1 = ['15', '20', '25', '30', '35']
xticks(x1, labels1)
xlim([-0.1, 4.1])
xlabel("shifted stim PN number")
ylabel("shifted resp PN number")

'''
if tend>2500: ylim([0, 15])
else: ylim([10, 30])
'''

savefig("barjumper_number_error_among_trial_%d_%d.jpg"%(tbgn,tend))
show()
