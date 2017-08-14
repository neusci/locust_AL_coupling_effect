execfile('../../slow/slow_analy_head.py')

c,s=0,0
cd=50
tb,te=1000,6000

xlist=transpose([load_sf_avged_over_trial(c,s, cf, cf+cd, cd)
                      for cf in range(tb, te, cd)])

print('loaded')

plot(xlist[0]);
plot(xlist[1]);
#plot(xlist[7]);
#plot(xlist[9]);
plot(xlist[12])
axvspan(xmin=2,xmax=5, facecolor='0.25', alpha=0.5)
axhline(xmin=0,xmax=0.5, y=-2.5, lw=4, color='gray')
xlim([0,100])
xlabel('time (ms)')
ylabel('fire rate (Hz)')
x1 = [0, 20, 40, 60, 80, 100]
labels1 = ['0', '1000','2000', '3000', '4000', '5000']
xticks(x1, labels1)
savefig('firerate_of_a_neuron_curves.jpg')
savefig('firerate_of_a_neuron_curves.eps')
clf()
