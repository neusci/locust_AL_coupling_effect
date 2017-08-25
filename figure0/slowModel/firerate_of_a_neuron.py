execfile('../../slow/slow_analy_head.py')

c,s=0,0
cd=50
tb,te=1000,6500

xlist=transpose([load_sf_avged_over_trial(c,s, cf, cf+cd, cd)
                      for cf in range(tb, te, cd)])

print('loaded')

aX=xlist[0]
bX=xlist[1]
cX=xlist[7]
dX=xlist[9]
eX=xlist[12]

plot(aX);
plot(bX);
#plot(cX);
#plot(dX);
plot(eX)

axvspan(xmin=2,xmax=7, facecolor='0.25', alpha=0.5)
axhline(xmin=0,xmax=0.5, y=-2.5, lw=4, color='gray')
xlim([0,110])
xlabel('time (ms)')
ylabel('fire rate (Hz)')
x1 = [0, 20, 40, 60, 80, 100]
labels1 = ['0', '1000','2000', '3000', '4000', '5000']
xticks(x1, labels1)
savefig('firerate_of_a_neuron_curves.jpg')
savefig('firerate_of_a_neuron_curves.eps')
clf()

# ---

aY=smooth(aX)
bY=smooth(bX)
cY=smooth(cX)
dY=smooth(dX)
eY=smooth(eX)

plot(aY);
plot(bY);
#plot(cY);
#plot(dY);
plot(eY)

axvspan(xmin=2,xmax=7, facecolor='0.25', alpha=0.5)
axhline(xmin=0,xmax=0.5, y=-2.5, lw=4, color='gray')
xlim([0,110])
xlabel('time (ms)')
ylabel('fire rate (Hz)')
x1 = [0, 20, 40, 60, 80, 100]
labels1 = ['0', '1000','2000', '3000', '4000', '5000']
xticks(x1, labels1)
savefig('firerate_of_a_neuron_curve_smoothed.jpg')
savefig('firerate_of_a_neuron_curve_smoothed.eps')
clf()
