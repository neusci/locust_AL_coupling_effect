#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


execfile('../slow/slow_analy_head.py')

slist=shift_list
offnet=array([load_sf_avged_over_trial(100,i,1100,1350,50) for i in slist])
onnet =array([load_sf_avged_over_trial(  0,i,1100,1350,50) for i in slist])

onsp=array([lifetimeSparseness(onnet[:,i]) for i in range(PN_number)])
offsp=array([lifetimeSparseness(offnet[:,i]) for i in range(PN_number)])


#plot(offsp); plot(onsp); show()
#plot(offsp[:250]); plot(onsp[:250]); show()

for i in range(0,250,10):
    print(i, offsp[i], onsp[i])

# 0   0.965455893254 0.23765339894
# 10  0.91596462037  0.0254901920665
#v20  0.816023161011 0.32485905964
#v30  0.727663634519 0.385368911495
#v40  0.665697115888 0.308393080984
#v50  0.562224296255 0.254942863269
#v60  0.459100182069 0.220950310162
#v70  0.414147294524 0.152823502949
# 80  0.309476208075 0.0841407943422
# 90  0.206366618517 0.113051595314
# 100 0.15415154265  0.0555469511584
# 110 0.054971336604 0.0185858453135
# 120 0.051001640670 0.0264871990073
# 130 0.109067823112 0.0385900715863
# 140 0.196311000379 0.0991969084595
# 150 0.315404708955 0.0621541718797
# 160 0.361915546973 0.0883915013633
# 170 0.468551142072 0.14149367346
#v180 0.566450372507 0.149770479277
#v190 0.606666390168 0.180109413755
#v200 0.705441045671 0.207079013228
#v210 0.809868223308 0.226237808789
#v220 0.868401472431 0.255037859432
#v230 0.945520581114 0.117752876562
# 240 0.536842105263 0.0394934903742


PNls=[20,30,40,50,60,70,180,190,200,210,220,230]
onsp_inls=onsp[PNls]
offsp_inls=offsp[PNls]
#figure(figsize=(10,2)) # set figure size -- this removes xlabel??

for i in rlen(PNls):
    plot([onsp_inls[i],offsp_inls[i]],[1,0], '-',c='gray')
    plot(onsp_inls[i], 1, 'o', c='r')
    plot(offsp_inls[i],0, 'o', c='b')

#ax1 = axes() # to hide yaxis
#ax1.axes.get_yaxis().set_visible(False)
#ax1.set_xlabel('lifetime sparseness')
xlabel('lifetime sparseness')
ylabel('')
y1 = [0, 1]
labels1 = ['offnet', 'onnet']
yticks(y1, labels1)  #, rotation='vertical')
savefig('./lifetimeSparseness.jpg')
savefig('./lifetimeSparseness.eps')
show()
clf()
