print("plot firerate in mini-timebins (5MS) in a trial")
x=loaddata(0,0,0)
pcolormesh(x);
xlabel("time (ms)"); ylabel("PN #")
savefig('mesh_of_a_trial.jpg');
#savefig('mesh_of_a_trial.eps');
clf()


x=load_sf_in_trial(0,0,0)
plot(x);
xlabel("time (ms)"); ylabel("fire rate")
savefig('sf_vs_time_in_a_trial.jpg');
savefig('sf_vs_time_in_a_trial.eps');
clf()
