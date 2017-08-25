execfile('../../slow/slow_analy_head.py')

xlist=[loaddata(0,0,i) for i in range(trial_number)]
print('loaded')

tb=1000
te=6500

# ---

def v_short_line_a_neuron(nid):
    for i in range(trial_number):
        x=xlist[i]
        for xi,xe in enum(x[nid, tb:te]):
            if xe>0:
                axvline(x=xi, ymin=0.02+i*0.1, ymax=0.08+i*0.1, lw=0.15)

    axhline(xmin=0,xmax=0.5,linewidth=4, color='gray')
    axvspan(xmin=100,xmax=350, facecolor='0.75', alpha=0.75)
    xlim([0,te-tb])
    axis('off')
    savefig('v_short_line_%d.jpg'%nid)
    savefig('v_short_line_%d.eps'%nid)
    clf()

# 12 9 7 1 0 # the neuron we are going to investigate

v_short_line_a_neuron(0)
v_short_line_a_neuron(1)
v_short_line_a_neuron(7)
v_short_line_a_neuron(9)
v_short_line_a_neuron(12)
