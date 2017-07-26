execfile("slow_analy_head.py")

tbgn=1100
tend=1350

print("plot the sorted mean of firerate and std of firerate (red dots ind stim)")
print("begin time=%d, end time=%d"%(tbgn,tend))

# all trials
xsum = zeros(PN_number)
ysum = zeros(PN_number)
for ccc in range(couple_number):
    x = load_sf_avged_over_trial(ccc, 0, tbgn, tend)
    y = load_sf_stded_over_trial(ccc, 0, tbgn, tend)
    tuples = sorted(zip(x, y), reverse=True)
    xnew, ynew = array([t[0] for t in tuples]), array([t[1] for t in tuples]) # mean and error
    xsum += xnew
    ysum += ynew

xsum /= (1.0*couple_number)
ysum /= (1.0*couple_number)

#tuplet = sorted(zip(x, range(PN_number)), reverse=True)
#xodr = [t[1] for t in tuplet]

fill_between(x=range(PN_number), y1=(xsum-1*ysum), y2=(xsum+1*ysum), alpha=0.2, color="#089FFF", antialiased=true)
plot(xsum, color="white", lw=2)

#for i in range(PN_number):
    #if xodr[i] < PN_stim_number:
        #plot(i, xnew[i], '.', color='r', markersize=2)

xlabel("PN #")
ylabel("sorted fire rate (Hz)")
xlim([0,PN_number])
#ylim([0,50])
savefig("sf_avg_var_%d_%d.jpg"%(tbgn,tend))
savefig("sf_avg_var_%d_%d.eps"%(tbgn,tend))
show()
clf()
