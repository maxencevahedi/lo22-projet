from fiabilipym import Component, System

s = System()

# Components
hba1 = Component("HBA1", 1.25 * 10**-6, 7e-3)
hba2 = Component("HBA2", 1.25 * 10**-6, 7e-3)
linka = Component("LINKA", 2.52 * 10**-6, 3e-3)
linkb = Component("LINKB", 2.52 * 10**-6, 3e-3)
hub = Component("HUB", 1.71 * 10**-6, 2e-3)
linkc = Component("LINKC", 2.52 * 10**-6, 3e-3)
linkd = Component("LINKD", 1.71 * 10**-6, 3e-3)
diska = Component("DISKA", 10**-5, 5e-4)
diskb = Component("DISKB", 10**-5, 5e-4)

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
pl.plot(timerange, reliability)
pl.title("1")
pl.show()
