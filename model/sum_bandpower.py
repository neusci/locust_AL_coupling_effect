bp0=loadtxt("bandpower_0_0.txt")
bp1=loadtxt("bandpower_1_0.txt")
bp2=loadtxt("bandpower_2_0.txt")
bp3=loadtxt("bandpower_3_0.txt")
bp_avg=(bp0+bp1+bp2+bp3)/4.0

x1 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
labels1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10']
xticks(x1, labels1)
# xlim([0,200])
xlabel("time (S)")
ylabel("bandpower")

rect = plt.Rectangle((20, 0), 50, 0.001, facecolor="0.4")
plt.gca().add_patch(rect)
fill_between(x=rlen(bp_avg), y1=map(min, zip(bp0,bp1,bp2,bp3)), y2=map(max, zip(bp0,bp1,bp2,bp3)), alpha=0.2, color="#089FFF", antialiased=true)
plot(bp_avg, color="m", lw=1.5)
savefig("sum_bandpower.jpg")
savefig("sum_bandpower.eps")
show()
