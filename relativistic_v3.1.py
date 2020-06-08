import numpy as np
from numpy import polyfit
import matplotlib.pyplot as plt
import math

#gamma = np.linspace(0,(np.pi)/2,200)


alpham = 4e-3 #convergence half angle ?
betam = 15e-3 #collection half angle ?

c=299792458

me=9.109*10**(-31)
Va=300000
e=1.602176634*10**(-19)

thetaEm=.38e-3 #average thetaE for B-K edge
y=1.5871
v=2.328*10**8
fa=(thetaEm**2)/y**2

def fr1(a,b,u,frac):
	f=a*b*(a**2+b**2-2*a*b*math.cos(u))/(a**2+b**2-2*a*b*math.cos(u)+frac)**2
	return f

#print(fr1(alpham,betam,math.pi,fa))

def dfr1u(a,b,u,frac):
	f=2*(a**2)*(b**2)*math.sin(u)*(frac-a**2-b**2+2*a*b*math.cos(u))/(frac+a**2+b**2-2*a*b*math.cos(u))**3
	return f
	
def dfr1a(a,b,u,frac):
	f=b*(a**2+b**2-2*a*b*math.cos(u))/(frac+a**2+b**2-2*a*b*math.cos(u))**2+2*a*b*(a-b*math.cos(u))*(frac-a**2-b**2+2*a*b*math.cos(u))/(frac+a**2+b**2-2*a*b*math.cos(u))**3
	return f
	
def dfr1b(a,b,u,frac):
	f=a*(a**2+b**2-2*a*b*math.cos(u))/(frac+a**2+b**2-2*a*b*math.cos(u))**2+2*a*b*(b-a*math.cos(u))*(frac-a**2-b**2+2*a*b*math.cos(u))/(frac+a**2+b**2-2*a*b*math.cos(u))**3
	return f
	
#print(dfr1u(alpham,betam,math.pi,fa))
#print(dfr1a(alpham,betam,math.pi,fa))
#print(dfr1b(alpham,betam,math.pi,fa))

def fr2(a,b,u,frac):
	f=a*b/(a**2+b**2-2*a*b*math.cos(u)+frac)**2
	return f

#print(fr2(alpham,betam,math.pi,fa))

ul=np.linspace(-np.pi,np.pi,300, endpoint=True) #h=(stop-start)/(N-1)
uh=2*np.pi/299
al=np.linspace(0,alpham,300,endpoint=True)
ah=alpham/299
bl=np.linspace(0,betam,300,endpoint=True)
bh=betam/299

ar1=0
for ai in al:
	br1=0
	for bi in bl:
		ur1=0
		for ui in ul:
			ur1=ur1+fr1(ai,bi,ui,fa)	
#			print(ur1)
		ur1=ur1-fr1(ai,bi,ul[0],fa)/2-fr1(ai,bi,ul[-1],fa)/2
		if (bi==bl[0]) or (bi==bl[-1]):
			br1=br1+uh*ur1*bh/2
		else:
			br1=br1+uh*ur1*bh
#		print(br1)
	if (ai==al[0]) or (ai==al[-1]):
		ar1=ar1+br1*ah/2
	else:
		ar1=ar1+br1*ah
#	print(ar1)
ar1=ar1/alpham**2
print(ar1)

ar2=0
for ai in al:
	br2=0
	for bi in bl:
		ur2=0
		for ui in ul:
			ur2=ur2+fr2(ai,bi,ui,fa)	
#			print(ur2)
		ur2=ur2-fr2(ai,bi,ul[0],fa)/2-fr2(ai,bi,ul[-1],fa)/2
		if (bi==bl[0]) or (bi==bl[-1]):
			br2=br2+uh*ur2*bh/2
		else:
			br2=br2+uh*ur2*bh
#		print(br2)
	if (ai==al[0]) or (ai==al[-1]):
		ar2=ar2+br2*ah/2
	else:
		ar2=ar2+br2*ah
#	print(ar2)
ar2=ar2*2*thetaEm**2/((y**4)*alpham**2)
print(ar2)

	






