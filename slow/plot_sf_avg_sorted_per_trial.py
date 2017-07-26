execfile("slow_analy_head.py")

tbgn=1100
tend=1350

print("plot the sorted firerate lists")
print("begin time=%d, end time=%d"%(tbgn,tend))

# all trials
for ccc in [0]:  #range(couple_number):
    for sss in shift_list:
        for ttt in range(trial_number):
            x = load_sf_from_file(ccc, sss, ttt, tbgn, tend, cd=50)
            xnew = sorted(x, reverse=True)
            plot(xnew)

xlabel("PN #")
ylabel("sorted fire rate (Hz)")
xlim([0,PN_number])
#ylim([0,50])
savefig("sf_avg_perTrial_%d_%d.jpg"%(tbgn,tend))
savefig("sf_avg_perTrial_%d_%d.eps"%(tbgn,tend))
show()
clf()
