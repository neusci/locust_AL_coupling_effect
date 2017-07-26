execfile("slow_analy_head.py")

print("corr between each PNs firerate in time regins [1100,1500] and in [1500,3500]")
print("     shift_list should be [0, 6, 12, ...] with the length being 20")
fplot('y=x',[0,35])
tb1=1200
te1=1500
tb2=1500
te2=3500

c=0
i=0;  plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[4]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[8]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[12]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[16]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)

c=1
i=0;  plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[4]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[8]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[12]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[16]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)

c=2
i=0;  plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[4]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[8]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[12]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[16]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)

c=3
i=0;  plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[4]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[8]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[12]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[16]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)

c=4
i=0;  plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[4]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[8]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[12]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)
i=shift_list[16]; plot(jittering(load_sf_avged_over_trial(c,i,tb1,te1),0.5,1),jittering(load_sf_avged_over_trial(c,i,tb2,te2),0.5,1), '.', markersize=3)

xlabel('fire rate in transition')
ylabel('fire rate in oscillation')
xlim([0,40])
ylim([0,40])
savefig("trans_osc_corr_%d_%d_%d_%d.jpg"%(tb1,te1,tb2,te2))
show()
clf()
