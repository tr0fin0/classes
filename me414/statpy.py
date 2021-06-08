import numpy as np
from scipy import special
from scipy.integrate import quad

def ccxy(x, y):
    if(x.size != y.size):
        return 2

    n = x.size

    xm = x.mean()
    ym = y.mean()

    sx = np.std(x, ddof=1)
    sy = np.std(y, ddof=1)

    zx = (x - xm)/sx
    zy = (y - ym)/sy

    ccxy = np.sum(zx*zy)/(n-1)

    return ccxy

def Combination(n, k):
    #n: number of objects
    #k: number of groups

    if n<k:
        return 0

    fatorialN = np.math.factorial(n)
    fatorialK = np.math.factorial(k)
    fatorialNK = np.math.factorial(n-k)

    cnk = fatorialN/(fatorialK*fatorialNK)

    return cnk

def Bernoulli(x, n, p):
    #x: = 1, sucess
    #   = 0, fail
    #p: probability of sucess
    #n: number of trials

    px = (p**(x))*((1-p)**(n-x))

    return px

def Binomial(x, n, p):
    #x: number of sucesses
    #n: number of trials
    #p: probability of sucess
    cnx = Combination(n, x)

    px = cnx*Bernoulli(x, n, p)

    return px

def BinomialInfo(x, n, p):
    #x: number of sucesses
    #n: number of trials
    #p: probability of sucess

    pxl = 0
    px = Binomial(x, n, p)

    for i in range(x):
        pxl += Binomial(i, n, p)

    expectedValue = n*p
    varianceValue = n*p*(1-p)

    print("\nBinomial Distribution")
    print("p = {:.4f}".format(p))
    print("n = {:.4f}".format(n))
    print("x = {:.4f}".format(x))
    print("E(X) = {:.4f}".format(expectedValue))
    print("V(X) = {:.4f}".format(varianceValue))
    print("P(X ={}) = {:.4f}".format(x, px))
    print("P(X<={}) = {:.4f}".format(x, px+pxl))
    print("P(X>={}) = {:.4f}".format(x, 1-pxl))
    print("P(X< {}) = {:.4f}".format(x, pxl))
    print("P(X> {}) = {:.4f}".format(x, 1-pxl-px))

    return px

def Geometric(x, p):
    #x: number of trials to sucess
    #p: probability of sucess

    px = p*(1-p)**(x-1)

    return px

def GeometricInfo(x, p):
    #x: number of trials to sucess
    #p: probability of sucess

    px = Geometric(x, p)

    pxl = 0
    for i in range(1,x):
        pxl += Geometric(i, p)

    expectedValue = 1/p
    varianceValue = (1-p)/(p**2)

    print("\nGeometric Distribution")
    print("p = {:.4f}".format(p))
    print("x = {:.4f}".format(x))
    print("E(X) = {:.4f}".format(expectedValue))
    print("V(X) = {:.4f}".format(varianceValue))
    print("P(X ={}) = {:.4f}".format(x, px))
    print("P(X<={}) = {:.4f}".format(x, px+pxl))
    print("P(X>={}) = {:.4f}".format(x, 1-pxl))
    print("P(X< {}) = {:.4f}".format(x, pxl))
    print("P(X> {}) = {:.4f}".format(x, 1-px-pxl))

    return px

def HiperGeometric(x, n, X, N):
    #x: number of elements with A selected
    #n: number of elements selected
    #X: total number of elements with A
    #N: total number of elements

    Xx = Combination(X, x)
    Nn = Combination(N, n)
    nx = Combination(N-X,n-x)

    px = Xx*nx/Nn

    return px

def HiperGeometricInfo(x, n, X, N):
    #x: number of elements with A selected
    #n: number of elements selected
    #X: total number of elements with A
    #N: total number of elements

    px = HiperGeometric(x, n, X, N)

    pxl = 0
    for i in range(x):
        pxl += HiperGeometric(i, n, X, N)

    expectedValue = n*X/N
    varianceValue = expectedValue*(1 - X/N)*(N-n)/(N-1)

    print("\nHiper Geometric Distribution")
    print("x = {:.4f}".format(x))
    print("n = {:.4f}".format(n))
    print("X = {:.4f}".format(X))
    print("N = {:.4f}".format(N))
    print("E(X) = {:.4f}".format(expectedValue))
    print("V(X) = {:.4f}".format(varianceValue))
    print("P(X ={}) = {:.4f}".format(x, px))
    print("P(X<={}) = {:.4f}".format(x, px+pxl))
    print("P(X>={}) = {:.4f}".format(x, 1-pxl))
    print("P(X< {}) = {:.4f}".format(x, pxl))
    print("P(X> {}) = {:.4f}".format(x, 1-pxl-px))

    return px

def Poisson(x, n, p):
    #x: number of sucesses
    #n: number of trials
    #p: probability of sucess

    Lambda = n*p

    if( (Lambda <= 7) | ( (n >= 20) & (p <= 0.05) ) ):
        px = (np.exp(-Lambda)*(Lambda)**(x))/np.math.factorial(x)

    return px

def PoissonInfo(x: int, n: int, p: int):
    #x: number of sucesses
    #n: number of trials
    #p: probability of sucess

    Lambda = n*p

    px = Poisson(x, n, p)

    pxl = 0
    for i in range(x):
        pxl += Poisson(i, n, p)

    print("\nPoisson Distribution")
    print("x = {:.4f}".format(x))
    print("n = {:.4f}".format(n))
    print("p = {:.4f}".format(p))
    print("E(X) = {:.4f}".format(Lambda))
    print("V(X) = {:.4f}".format(Lambda))
    print("P(X ={}) = {:.4f}".format(x, px))
    print("P(X<={}) = {:.4f}".format(x, px+pxl))
    print("P(X>={}) = {:.4f}".format(x, 1-pxl))
    print("P(X< {}) = {:.4f}".format(x, pxl))
    print("P(X> {}) = {:.4f}".format(x, 1-pxl-px))


    return px

def Exponencial(Lambda: int, x: int):

    if (Lambda < 0):
        return 0

    return (1 - np.exp(-Lambda*x))

def ExponencialReverseL(x: int, p: float):

    if (p > 1):
        return 0

    Lambda = (-np.log(1-p))/x

    print("\nExponencial Reverse Lambda")
    print("x = {:.4f}".format(x))
    print("p = {:.4f}".format(p))
    print("l = {:.4f}".format(Lambda))

    return Lambda

def ExponencialReverseX(Lambda: float, p: float):

    if (p > 1):
        return 0

    x = (-np.log(1-p))/Lambda

    print("\nExponencial Reverse X")
    print("x = {:.4f}".format(x))
    print("p = {:.4f}".format(p))
    print("l = {:.4f}".format(Lambda))

    return x

def ExponencialInfo(Lambda: int, x: int):

    expectedValue = 1/Lambda
    varianceValue = 1/(Lambda**2)

    px = Exponencial(Lambda, x)

    print("\nExponencial Distribution")
    print("x      = {:.4f}".format(x))
    print("lambda = {:.4f}".format(Lambda))
    print("E(X) = {:.4f}".format(expectedValue))
    print("V(X) = {:.4f}".format(varianceValue))
    print("P(X<={}) = {:.4f}".format(x, px))
    print("P(X> {}) = {:.4f}".format(x, 1-px))

    return px

def NormalStandard(x: float):
    # x: number expected
    #
    # px: P(X < x)

    return 1/2*(special.erf(x/(np.sqrt(2))) + 1)

def NormalStandardInfo(x: float, s: int):
    #x: number expected
    #s: comparsion
    #   if (s == 1):
    #       P(X>x)
    #   if (s == -1):
    #       P(X<x)
    #   comparsion

    px = NormalStandard(x)

    print("\nNormal Standard Distribution")
    print("x    = {:.4f}".format(x))

    #equals zero
    if(s == 0):
        return 0

    #P(X < x) where x is positive
    if ((s == -1) & (x > 0)):
        print("P(X<={}) = {:.4f}".format(x, px))

    #P(X < x) where x is negative
    elif((s == -1) & (x < 0)):
        print("P(X<={}) = {:.4f}".format(x, px))

    #P(X > x) where x is positive
    elif((s == 1) & (x > 0)):
        print("P(X>={}) = {:.4f}".format(x, 1-px))

    #P(X > x) where x is negative
    elif((s == 1) & (x < 0)):
        print("P(X>={}) = {:.4f}".format(x, 1-px))

    return px

def NormalStandardIntervalInfo(a: float, b: float):

    pa = NormalStandard(a)
    pb = NormalStandard(b)

    px = pb - pa

    # print("\nNormal Standard Interval Distribution")
    # print("a = {:.4f} and b = {:.4f}".format(a,b))
    # print("E(X) = 0 and V(X) = 1")
    print("P({:.4f} < Z < {:.4f}) = {:.4f}".format(a, b, px))

    return px


def Normal(x: float, mu: float, sg: float):
    return NormalStandard((x - mu)/np.sqrt(sg))

def NormalInfo(x: float, mu: float, sg: float, s: int):
    # x:  number expected
    # mu: expected value
    # sg: variance value
    # s:  comparsion
    #
    #   if (s == 1):
    #       P(X>x)
    #   if (s == -1):
    #       P(X<x)
    #   comparsion

    px = Normal(x, mu, sg)

    print("\nNormal Distribution")
    print("x    = {:.4f}".format(x))

    #equals zero
    if(s == 0):
        return 0

    #P(X < x) where x is positive
    if ((s == -1) & (x > 0)):
        print("P(X<={}) = {:.4f}".format(x, px))

    #P(X < x) where x is negative
    elif((s == -1) & (x < 0)):
        print("P(X<={}) = {:.4f}".format(x, px))

    #P(X > x) where x is positive
    elif((s == 1) & (x > 0)):
        print("P(X>={}) = {:.4f}".format(x, 1-px))

    #P(X > x) where x is negative
    elif((s == 1) & (x < 0)):
        print("P(X>={}) = {:.4f}".format(x, 1-px))

    return px

def NormalIntervalInfo(a: float, b: float, mu: float, sg: float):
    # P(a < X < b)
    # mu: expected value
    # sg: variance value

    pa = Normal(a, mu, sg)
    pb = Normal(b, mu, sg)

    px = pb - pa

    print("\nNormal Interval Distribution")
    print("a = {:.4f} and b = {:.4f}".format(a,b))
    print("E(X) = 0 and V(X) = 1")
    print("P({:.4f} < Z < {:.4f}) = {:.4f}".format(a, b, px))

    return px

def NormalStandardReverse(px: float):
    # px: P(X < x)
    #
    # x: expected value

    return np.sqrt(2)*special.erfinv(2*px - 1)

def NormalStandardReverseInfo(px: float, s: int, m: int):
    # px: number expected
    #  s: comparsion
    #   if (s == 1):
    #       P(X>x)
    #   if (s == -1):
    #       P(X<x)
    #   comparsion
    #
    #  m: module
    #   if (m == 1):
    #       P(|X| > x) or P(|X| < x)
    #   if (s == 0):
    #       P(X > x) or P(X < x)
    #   comparsion

    # |A| > a: A > a or A < -a
    # |A| < a: A < a or A > -a, -a < A < a

    # print("\nNormal Standard Reverse Distribution")
    # print("px = {:.4f}".format(x))

    #equals zero
    if(s == 0):
        return 0

    #P(X < x) = px
    if ((s == -1) & (m == 0)):
        x = NormalStandardReverse(px)
        print("P(X < {:.4f}) = {:.4f}".format(x, px))

    #P(|X| < x) = px
    elif((s == -1) & (m == 1)):
        x = NormalStandardReverse((1+px)/2)
        print("P(|X| < {:.4f}) = {:.4f}".format(x, px))

    #P(X > x) = px
    elif((s == 1) & (m == 0)):
        x = NormalStandardReverse(1-px)
        print("P(X > {:.4f}) = {:.4f}".format(x, px))

    #P(|X| > x) = px
    elif((s == 1) & (m == 1)):
        x = NormalStandardReverse(1-px/2)
        print("P(|X| > {:.4f}) = {:.4f}".format(x, px))

    return x

def NormalReverse(px: float, mu: float, sg: float):
    # px: probability P(X < x)
    # mu: expected value
    # sg: variance value

    # print("\nNormal Reverse Distribution")
    # print("px = {:.4f}".format(x))

    return (mu + np.sqrt(sg)*NormalStandardReverse(px))

def NormalReverseInfo(px: float, mu: float, sg: float):
    # px: probability P(X < x)
    # mu: expected value
    # sg: variance value

    print("\nNormal Reverse Distribution")

    x = NormalReverse(px, mu, sg)

    print("P(X < {:.2f}) = {:.4f}: E(X) = {} and V(X) = {}".format(px, x, mu, sg))

    return x