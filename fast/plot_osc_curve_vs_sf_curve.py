tbgn=1200
tend=1500
dLen=5

print('This is used to check if more PNs spike at osc peaks')


c=0
print(c)
d=map(mean, equally_divide(sum(loaddata(c,0,0),0)[tbgn:tend],dLen))
x=load_sf_in_trial(c,0,0,cd=dLen)[int(round(tbgn/dLen)):int(round(tend/dLen))]
plot((array(d)+50000)/1000.0); plot(x);
xlabel('time (S)'); ylabel('firing rates and oscillation voltage');
x_tick = [0,20,40,60]
x_tick_labels = [1.2, 1.3, 1.4, 1.5]
xticks(x_tick, x_tick_labels)
savefig('osc_highlow_vs_firerate_%d_%d.jpg'%(tbgn,tend));
savefig('osc_highlow_vs_firerate_%d_%d.eps'%(tbgn,tend))
clf()
plot(d,x,'.');


c=1
print(c)
d=map(mean, equally_divide(sum(loaddata(c,0,0),0)[tbgn:tend],dLen))
x=load_sf_in_trial(c,0,0)[int(round(tbgn/dLen)):int(round(tend/dLen))]
plot(d,x,'.');


c=2
print(c)
d=map(mean, equally_divide(sum(loaddata(c,0,0),0)[tbgn:tend],dLen))
x=load_sf_in_trial(c,0,0)[int(round(tbgn/dLen)):int(round(tend/dLen))]
plot(d,x,'.');


c=3
print(c)
d=map(mean, equally_divide(sum(loaddata(c,0,0),0)[tbgn:tend],dLen))
x=load_sf_in_trial(c,0,0)[int(round(tbgn/dLen)):int(round(tend/dLen))]
plot(d,x,'.');


c=4
print(c)
d=map(mean, equally_divide(sum(loaddata(c,0,0),0)[tbgn:tend],dLen))
x=load_sf_in_trial(c,0,0)[int(round(tbgn/dLen)):int(round(tend/dLen))]
plot(d,x,'.');

xlabel('voltage of oscillation')
ylabel('firing rate of all PNs')

savefig('osc_curve_vs_firerate_curve_%d_%d.jpg'%(tbgn,tend));
savefig('osc_curve_vs_firerate_curve_%d_%d.eps'%(tbgn,tend));
clf()
