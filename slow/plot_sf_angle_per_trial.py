execfile("slow_analy_head.py")

tbgn=1100
tend=1350

print("plot the angle between firerate vectors")
print("begin time=%d, end time=%d"%(tbgn,tend))

# to compute the included angle
def iang(u,v):
    return degrees(arccos(clip(dot(1.0*u/norm(u), 1.0*v/norm(v)), -1.0, 1.0)))
                  # np.dot,clip,arccos,degrees;  np.linalg.norm

# all trials
x=[]
for ccc in range(couple_number):
    for sss in [0]:  # shift_list:
        for ttt in range(trial_number):
            x.append(load_sf_from_file(ccc, sss, ttt, tbgn, tend, cd=50))

a=[]
print(len(x))
for i,j in muloop([len(x), len(x)]):
    if i>=j: continue
    a.append(iang(x[i], x[j]))

plot(a, '.-')
xlabel("#")
ylabel("included angles")
savefig("sf_angle_perTrial_%d_%d.jpg"%(tbgn,tend))
savefig("sf_angle_perTrial_%d_%d.eps"%(tbgn,tend))
#show()
clf()

hist(a, normed=1)
xlabel("included angles")
ylabel("ratio")
savefig("sf_angle_hist_perTrial_%d_%d.jpg"%(tbgn,tend))
savefig("sf_angle_hist_perTrial_%d_%d.eps"%(tbgn,tend))
#show()
clf()
