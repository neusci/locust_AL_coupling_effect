#  !/usr/bin/env python
#  -*- coding:utf-8 -*-


BG_input_rate         = 3.50000
ORN_input_rate        = 0.03500
BG_input_strength_PN  = 0.06100
BG_input_strength_LN  = 0.00010
ORN_input_strength_PN = 0.01840
ORN_input_strength_LN = 0.01760
ORN_number            = 200


def ORN2neuron(t, each): # use abs time, odor onset at 1th sec.
    t0 = 1000  # in ms
    ts = 400
    td = 3500
    c1 = 100000
    c2 = sqrt(1000)
    # ...
    if t <= t0: x = 0
    elif t0 < t <= (t0+ts): x = ORN_input_rate*each*exp(-(t-t0-ts)**2/c1)
    elif (t0+ts) < t <= td: x = ORN_input_rate*each
    else: x = ORN_input_rate*each*exp(-sqrt(t-td)/c2)
    return x*ORN_number*5 # 5 is the living time of sync currents #200ORN

def BG2neuron(each):
    return each*BG_input_rate*5 # 5 is currents living time

def ORN2PN(t):
    return ORN2neuron(t,-ORN_input_strength_PN)

def ORN2LN(t):
    return ORN2neuron(t,-ORN_input_strength_LN)

def BG2PN(t):
    return BG2neuron(-BG_input_strength_PN)

def BG2LN(t):
    return BG2neuron(-BG_input_strength_LN)

def input2PN(t):
    return ORN2PN(t)+BG2PN(t)

def input2LN(t):
    return ORN2LN(t)+BG2LN(t)

def integrate_input2PN(t0,t1):
    return abs(sp.integrate.quad(input2PN, t0, t1)[0])

def integrate_BG2PN(t0,t1):
    return abs(sp.integrate.quad(BG2PN, t0, t1)[0])

def integrate_input2LN(t0,t1):
    return abs(sp.integrate.quad(input2LN, t0, t1)[0])

def integrate_BG2LN(t0,t1):
    return abs(sp.integrate.quad(BG2LN, t0, t1)[0])


xx=linspace(0,10000, 1000) # 10S, 1000 regions
x_tick_labels = [0,1,2,3,4,5,6,7,8,9,10]
x_tick = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

yP=map(input2PN, xx)
plot(xx,yP);
xticks(x_tick, x_tick_labels)
xlabel("time (second)")
ylabel("input (ORN+BG) current (uA)")
savefig("input2PN.eps")
savefig("input2PN.jpg")
show()

yBP=map(BG2PN, xx)
plot(xx,yBP);
xticks(x_tick, x_tick_labels)
xlabel("time (second)")
ylabel("background current (uA)")
savefig("BG2PN.eps")
savefig("BG2PN.jpg")
show()
