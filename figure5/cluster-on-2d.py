execfile('../slow/slow_analy_head.py')

idx = range(PN_number)
tb = 1100
te = 1350
use_num = 150  # use how many PNs
print('use %d PNs'%use_num)
use_idx = choice(idx,use_num) # PNs in use
print('PNs:',use_idx)
#use_slist = [0,18,42,72,108]  # shifts
#use_slist = [0,12, 30, 60,90]  # shifts
use_slist = [0, 12, 24, 36, 48]  # shifts
print('use shifts',use_slist)

c0='b'  #'sage'
c1='g'  #'orange'
c2='r'  #'royalblue'
c3='c'  #'pink'
c4='m'  #'rosybrown'
# for name, hex in matplotlib.colors.cnames.items():
#     print(name)


if __name__ == '__main__':
    c = 0
    sprate_ls = [load_sf_avged_over_trial(c,s,tb,te)[use_idx] for s in use_slist]
    for s in use_slist:
        for t in range(trial_number):
            sprate_ls.append(load_sf_from_file(c,s,t,1100,1350)[use_idx])

    y=PCA(sprate_ls, 2)
    plot(y[0,0], y[0,1], 'o', ms=6, c=c0)
    plot(y[1,0], y[1,1], 'o', ms=6, c=c1)
    plot(y[2,0], y[2,1], 'o', ms=6, c=c2)
    plot(y[3,0], y[3,1], 'o', ms=6, c=c3)
    plot(y[4,0], y[4,1], 'o', ms=6, c=c4)

    ttt=0
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '8', ms=4, c=c0)

    ttt=1
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], 'x', ms=4, c=c1)

    ttt=2
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '+', ms=4, c=c2)

    ttt=3
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '^', ms=4, c=c3)

    ttt=4
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '*', ms=4, c=c4)

    title('couple %d, use %d PNs'%(c,use_num))
    savefig('classification_2d_c%d_%dPNs.jpg'%(c,use_num))
    savefig('classification_2d_c%d_%dPNs.eps'%(c,use_num))
    show()

    # ----

    c = 100
    sprate_ls = [load_sf_avged_over_trial(c,s,tb,te)[use_idx] for s in use_slist]
    for s in use_slist:
        for t in range(trial_number):
            sprate_ls.append(load_sf_from_file(c,s,t,1100,1350)[use_idx])

    y=PCA(sprate_ls, 2)
    plot(y[0,0], y[0,1], 'o', ms=6, c=c0)
    plot(y[1,0], y[1,1], 'o', ms=6, c=c1)
    plot(y[2,0], y[2,1], 'o', ms=6, c=c2)
    plot(y[3,0], y[3,1], 'o', ms=6, c=c3)
    plot(y[4,0], y[4,1], 'o', ms=6, c=c4)

    ttt=0
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '8', ms=4, c=c0)

    ttt=1
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], 'x', ms=4, c=c1)

    ttt=2
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '+', ms=4, c=c2)

    ttt=3
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '^', ms=4, c=c3)

    ttt=4
    for i in range(len(use_slist)+ttt*trial_number, len(use_slist)+(ttt+1)*trial_number):
        plot(y[i,0], y[i,1], '*', ms=4, c=c4)

    title('couple %d, use %d PNs'%(c,use_num))
    savefig('classification_2d_c%d_%dPNs.jpg'%(c,use_num))
    savefig('classification_2d_c%d_%dPNs.eps'%(c,use_num))
    show()
