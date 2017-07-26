sort0=loadtxt("sorted_0_0.txt")
sort1=loadtxt("sorted_1_0.txt")
sort2=loadtxt("sorted_2_0.txt")
sort3=loadtxt("sorted_3_0.txt")
sort_avg=(sort0+sort1+sort2+sort3)/4.0

xlabel("sorted PN #")
ylabel("fire rate (Hz)")

fill_between(x=rlen(sort_avg), y1=map(min, zip(sort0,sort1,sort2,sort3)), y2=map(max, zip(sort0,sort1,sort2,sort3)), alpha=0.2, color="#089FFF", antialiased=true)
plot(sort_avg, color="m", lw=1.5)
savefig("sum_sorted.jpg")
savefig("sum_sorted.eps")
show()
