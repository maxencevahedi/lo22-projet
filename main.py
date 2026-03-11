from fiabilipym import Component, System
from sympy import Symbol

s = System()

# Components
hba1 = Component("HBA1", 1.25 * 10**-6)
hba2 = Component("HBA2", 1.25 * 10**-6)
linka = Component("LINKA", 2.52 * 10**-6)
linkb = Component("LINKB", 2.52 * 10**-6)
hub = Component("HUB", 1.71 * 10**-6)
linkc = Component("LINKC", 2.52 * 10**-6)
linkd = Component("LINKD", 1.71 * 10**-6)
diska = Component("DISKA", 10**-5)
diskb = Component("DISKB", 10**-5)

# System
s["E"] = [hba1, hba2]

s[hba1] = linka
s[hba2] = linkb

s[linka] = s[linkb] = hub

s[hub] = [linkc, linkd]

s[linkc] = diska
s[linkd] = diskb

s[diska] = s[diskb] = "S"

import pylab as pl

timerange = range(0, 2 * 365 * 24, 1)
reliability = [s.reliability(t) for t in timerange]
availability = [s.availability(t) for t in timerange]

pl.plot(timerange, availability)
pl.show()
