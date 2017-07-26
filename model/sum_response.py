resp0=loadtxt("response_0_0.txt")
resp1=loadtxt("response_1_0.txt")
resp2=loadtxt("response_2_0.txt")
resp3=loadtxt("response_3_0.txt")
resp_avg=(resp0+resp1+resp2+resp3)/4.0

x1 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
labels1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10']
xticks(x1, labels1)
# xlim([0,200])
xlabel("time (S)")
ylabel("response ratio (%)")

rect = plt.Rectangle((20, 0), 50, 1, facecolor="0.4")
plt.gca().add_patch(rect)
fill_between(x=rlen(resp_avg), y1=map(min, zip(resp0,resp1,resp2,resp3)), y2=map(max, zip(resp0,resp1,resp2,resp3)), alpha=0.2, color="#089FFF", antialiased=true)
plot(resp_avg, color="m", lw=1.5)
savefig("sum_response.jpg")
savefig("sum_response.eps")
show()
