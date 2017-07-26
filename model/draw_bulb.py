ion() #https://github.com/matplotlib/matplotlib/issues/3139/

# draw the bulb
# http://www.mdpi.com/sensors/sensors-13-09344/article_deploy/html/images/sensors-13-09344f4-1024.png
# http://www.geocities.jp/nyjp07/index_egg_by_Itou_E.html in use
# http://www.geocities.jp/nyjp07/index_egg_by_SuudokuJuku_E.html
t=arange(68.5,89.5,0.1)/pi
a,b=0.260,0.240
x=a*cos(t)
y=b*sin(t)*cos(t/4)
axes().set_aspect('equal', 'datalim')
plot(y,x+0.05, c='gray', lw=1.5) # a standing egg is better


# show PNs and LNs
text(-0.15, 0.15, 'PN', color='r', bbox=dict(boxstyle="Circle", ec='r', fc="w"))
text(-0.15,-0.05, 'PN', color='r', bbox=dict(boxstyle="Circle", ec='r', fc="w"))
text( 0.1 , 0.15, 'LN', color='b', bbox=dict(boxstyle="Circle", ec='b', fc="w"))
text( 0.1 ,-0.05, 'LN', color='b', bbox=dict(boxstyle="Circle", ec='b', fc="w"))


# print ORN
text(-0.04, -0.35, 'ORNs', style='normal', color='r') #'purple')# bbox={'facecolor':'purple', 'alpha':0.5, 'pad':10})


# ORNs to PNs and LNs
# NOTE: arraws are from xytext to xy
annotate("",    xy=(-0.1, -0.078), #xycoords='axes points',
                xytext=(-0.01, -0.3), #textcoords='axes points',
                arrowprops=dict(arrowstyle="->", #  ->  -[
                                color='r', #"purple",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                # linestyle="dashed",
                                ),)


annotate("",    xy=( 0.1, -0.068), #xycoords='axes points',
                xytext=(0.01, -0.3), #textcoords='axes points',
                arrowprops=dict(arrowstyle="->", #  ->  -[
                                color='r', #"purple",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                # linestyle="dashed",
                                ),)


# print MB
text(-0.40, 0.275, 'MB', style='normal', color='gray') #'purple')# bbox={'facecolor':'purple', 'alpha':0.5, 'pad':10})


# PNs to MB
annotate("",    xy=(-0.325, 0.30), #xycoords='axes points',
                xytext=(-0.15, 0.2), #textcoords='axes points',
                arrowprops=dict(arrowstyle="->", #  ->  -[
                                color="r",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                # linestyle="dashed",
                                ),)


# LNs to PNs and LNs
annotate("",    xy=(0.13, 0.015), #xycoords='axes points',
                xytext=(0.13, 0.115), #textcoords='axes points',
                arrowprops=dict(arrowstyle="-[", #  ->  -[
                                color="b",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                #linestyle="dashed",
                                ),)


annotate("",    xy=(-0.06, 0.165), #xycoords='axes points',
                xytext=(0.085, 0.165), #textcoords='axes points',
                arrowprops=dict(arrowstyle="-[", #  ->  -[
                                color="b",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                #linestyle="dashed",
                                ),)


annotate("",    xy=(-0.06, -0.035), #xycoords='axes points',
                xytext=(0.085, -0.035), #textcoords='axes points',
                arrowprops=dict(arrowstyle="-[", #  ->  -[
                                color="b",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                #linestyle="dashed",
                                ),)


# PN to PNs and LNs
annotate("",    xy=(-0.1175, 0.1215), #xycoords='axes points',
                xytext=(-0.1175, 0.0125), #textcoords='axes points',
                arrowprops=dict(arrowstyle="->", #  ->  -[
                                color="r",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                # linestyle="dashed",
                                ),)


annotate("",    xy=(0.1125, 0.1275), #xycoords='axes points',
                xytext=(-0.1, 0.01), #textcoords='axes points',
                arrowprops=dict(arrowstyle="->", #  ->  -[
                                color="r",
                                linewidth = 1.2,
                                shrinkA=0, shrinkB=0,
                                patchA=None, patchB=None,
                                # linestyle="dashed",
                                ),)


# print AL
text(0.235, 0.05, 'AL', style='normal', color='gray')


xlim([-0.65, 0.6])
ylim([-0.4, 0.4])
axis('off') # hide all the axis related things
savefig("the_bulb.jpg")
savefig("the_bulb.eps")
show()
exit()
