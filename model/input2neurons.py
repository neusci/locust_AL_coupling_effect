#! /usr/bin/env python3

def ORN2neuron(t, each):
    t0 = 1000  # in ms
    ts = 400
    td = 3500
    c1 = 100000
    c2 = sqrt(1000)
    # ...
    if t <= t0: x = 0
    elif t0 < t <= (t0+ts): x = 0.035*each*exp(-(t-t0-ts)**2/c1)
    elif (t0+ts) < t <= td: x = 0.035*each
    else: x = 0.035*each*exp(-sqrt(t-td)/c2)
    return x*200*5 # 5 is the living time of sync currents #200ORN

def BG2neuron(each): return each*3.5*5 # 5 is currents living time

def input2PN(t): return ORN2neuron(t,-0.01743)+BG2neuron(-0.0654)

def input2LN(t): return ORN2neuron(t,-0.01667)+BG2neuron(-0.0001)

"""
execfile("input_curves.py")
xx=linspace(0,10000) # 10S

x_tick_labels = [0,1,2,3,4,5,6,7,8,9,10]
x_tick = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

yP=map(input2PN, xx)
a=loadtxt("./0/doc_stim_PN.txt")[1:,1:];
plot(sum(a[:,:33],1)/33); plot(xx,yP);
xticks(x_tick, x_tick_labels)
xlabel("time (second)")
ylabel("input current (uA)")
savefig("input2PN.eps")
savefig("input2PN.jpg")
show()

yL=map(input2LN, xx)
b=loadtxt("./0/doc_stim_LN.txt")[1:,1:];
plot(sum(b[:,:12],1)/12); plot(xx,yL);
xticks(x_tick, x_tick_labels)
xlabel("time (second)")
ylabel("input current (uA)")
savefig("input2LN.eps")
savefig("input2LN.jpg")
show()
"""
