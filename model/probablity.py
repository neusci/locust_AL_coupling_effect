def myFactorial(n):
    if n<=1000: return math.factorial(n)
    else: return sqrt(2*pi*n) * (n/e)**n

def CC(a,b): # combination
    if b>a: return 0
    elif b==a: return 1
    else:
        return myFactorial(a)/(myFactorial(b)*myFactorial(a-b))

def pick(M,k):
    '''
    There are 830 PNs in total, among which $m$ PNs fires. Randomly pick 415 PNs (a KC randomly connected to 415 PNs), the probability that $k$ PNs fire is $\frac{C(m,k) C(830-m,415-k)}{C(830,415)}$, where $C(x,y)=\frac{x!}{y! (x-y)!}$.
    '''
    if k>M: return 0
    else: return (CC(M,k)*CC(830-M,415-k))/CC(830,415)

def KCfp(m, th):
    # fire probabilities for given th(threshold)
    # a value is returned for the given PNs fire number m
    return sum([pick(m,i) for i in range(830) if i>=th])

th=50; print(th); plot([KCfp(x,th) for x in range(300)])
th=60; print(th); plot([KCfp(x,th) for x in range(300)])
th=70; print(th); plot([KCfp(x,th) for x in range(300)])
th=80; print(th); plot([KCfp(x,th) for x in range(300)])
text(90     ,   0.15, '50', alpha=0.75)
text(145    ,   0.15, '80', alpha=0.75)
xlim([50, 150])
ylim([0, 0.25])
xlabel("total active PN number")
ylabel("KCs spike ratio")
savefig("prob.jpg")
savefig("prob.eps")
# show()
clf()
