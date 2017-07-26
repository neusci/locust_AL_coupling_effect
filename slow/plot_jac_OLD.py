execfile("../slow/slow_analy_head.py")

tbgn=1100
tend=3500
th=30

print("odor decorr in AL")
print("begin time=%d, end time=%d, th=%d"%(tbgn,tend,th))
ols=[sets_divergence(odor_IDs(0), odor_IDs(i)) for i in shift_list]  # odor dist list


c=0
print(c)
xls=[filter_active_PN_from_sf(c,s,tbgn,tend,th) for s in shift_list]
dls=[sets_divergence(xls[0], i) for i in xls]  # diverg list
plot(append(ols,1), append(dls,1), '.-')
#plot(shift_list[1:], [100.0*dls[i+1]/shift_list[i+1] for i in range(len(shift_list)-1)], '.')


c=1
print(c)
xls=[filter_active_PN_from_sf(c,s,tbgn,tend,th) for s in shift_list]
dls=[sets_divergence(xls[0], i) for i in xls]
plot(append(ols,1), append(dls,1), '.-')
#plot(shift_list[1:], [100.0*dls[i+1]/shift_list[i+1] for i in range(len(shift_list)-1)], '.')


c=2
print(c)
xls=[filter_active_PN_from_sf(c,s,tbgn,tend,th) for s in shift_list]
dls=[sets_divergence(xls[0], i) for i in xls]
plot(append(ols,1), append(dls,1), '.-')
#plot(shift_list[1:], [100.0*dls[i+1]/shift_list[i+1] for i in range(len(shift_list)-1)], '.')


c=3
print(c)
xls=[filter_active_PN_from_sf(c,s,tbgn,tend,th) for s in shift_list]
dls=[sets_divergence(xls[0], i) for i in xls]
plot(append(ols,1), append(dls,1), '.-')
#plot(shift_list[1:], [100.0*dls[i+1]/shift_list[i+1] for i in range(len(shift_list)-1)], '.')


c=4
print(c)
xls=[filter_active_PN_from_sf(c,s,tbgn,tend,th) for s in shift_list]
dls=[sets_divergence(xls[0], i) for i in xls]
plot(append(ols,1), append(dls,1), '.-')
#plot(shift_list[1:], [100.0*dls[i+1]/shift_list[i+1] for i in range(len(shift_list)-1)], '.')


fplot("y=x")
xlim([0,1])
ylim([0,1])
xlabel("stimulation divergence")
ylabel("representation divergence (%)")
savefig("decorr_OLD_th%d_%d_%d.jpg"%(th,tbgn,tend))
show()
