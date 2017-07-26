execfile("import_all.py")
for i in range(couple_number):
    a=filter_active_PN(loadsf(i,0,0,1100,3500), 35)
    b=filter_active_PN(loadsf(i,1,0,1100,3500), 35)
    c=filter_active_PN(loadsf(i,2,0,1100,3500), 35)
    d=filter_active_PN(loadsf(i,4,0,1100,3500), 35)
    e=filter_active_PN(loadsf(i,8,0,1100,3500), 35)
    # ...
    d1=sets_divergence(a,b)
    d2=sets_divergence(a,c)
    d3=sets_divergence(a,d)
    d4=sets_divergence(a,e)
    # ...
    print(i,": \t %.5s \t %.5s \t %.5s \t %.5s"%(d1,d2,d3,d4))
    if min(d1,d2,d3,d4)<0.09:
        print("\t`-- Not Good")
