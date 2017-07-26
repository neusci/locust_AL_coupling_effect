sr0=loadtxt("spike_rate_0_0.txt")
sr1=loadtxt("spike_rate_1_0.txt")
sr2=loadtxt("spike_rate_2_0.txt")
sr3=loadtxt("spike_rate_3_0.txt")
sr_avg=(sr0+sr1+sr2+sr3)/4.0

x1 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
labels1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10']
xticks(x1, labels1)
# xlim([0,200])
xlabel("time (S)")
ylabel("fire rate (Hz)")

rect = plt.Rectangle((20, 0), 50, 0.4, facecolor="0.4")
plt.gca().add_patch(rect)
fill_between(x=rlen(sr_avg), y1=map(min, zip(sr0,sr1,sr2,sr3)), y2=map(max, zip(sr0,sr1,sr2,sr3)), alpha=0.2, color="#089FFF", antialiased=true)
plot(sr_avg, color="m", lw=1.5)
savefig("sum_sprate.jpg")
savefig("sum_sprate.eps")
show()
