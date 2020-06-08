import numpy as np
from numpy import polyfit
import matplotlib.pyplot as plt
import math

delta = np.linspace(0,(np.pi)/2,100)
delta2=delta+3*delta
#print(delta2)
##[261] corresponds to delta=63.40 degrees
ar1=11.371120
ar2=1.24684030
xref=ar1*(1+(math.cos(63.4*(np.pi)/180))**2) +ar2*(math.sin(63.4*(np.pi)/180))**2
yref=ar1*(math.sin(63.4*(np.pi)/180))**2 +ar2*(math.cos(63.4*(np.pi)/180))**2
Rref=.252889
s=(1/Rref-1)*yref/xref
print(xref)
print(yref)
print(s)

x=[]
y=[]
R=[]
i=0
for d in delta:
	x.append(ar1*(1+(math.cos(d))**2) +ar2*(math.sin(d))**2)
	y.append(ar1*(math.sin(d))**2 +ar2*(math.cos(d))**2)
	R.append(1/(1+s*x[i]/y[i]))
	i=i+1

#x=ar1*(1+(np.cos(delta*(np.pi)/180))**2) +ar2*(np.sin(delta*(np.pi)/180))**2
#y=ar1*(np.sin(delta*(np.pi)/180))**2 +ar2*(np.cos(delta*(np.pi)/180))**2
#print(x)

#Ipi = ((np.pi**2)/4)*((1 - np.cos(2*gamma))*(Bpi*beta**2 + Api*alpha0**2) + 2*np.cos(2*gamma)*(omegasqrpi - Wpi))
#Isigma = ((np.pi**2)/4)*((3 + np.cos(2*gamma))*(Bsigma*beta**2 + Asigma*alpha0**2) - 2*(1 + np.cos(2*gamma))*(omegasqrsigma - Wsigma))

#RWpi = Ipi/(Ipi + Isigma)
#R=1/(1+s*x/y)
#RWsigma = Isigma/(Ipi + Isigma)


thetaExp=[0,6*(np.pi)/180,16*(np.pi)/180,26*(np.pi)/180,31*(np.pi)/180,41*(np.pi)/180,46*(np.pi)/180,56*(np.pi)/180,63.4*(np.pi)/180,66*(np.pi)/180]
RWpiExp=[0,0.0479,0.05629,0.0730,0.0895,0.1295,0.1847,0.1590,0.252889,0.2224]




fig = plt.figure()
axes = fig.add_subplot(111, aspect='auto', adjustable='box-forced')
axes.plot(delta,R,color='blue', linestyle=':',
  label="RWpi_calculated")

#axes.plot(delta,RWsigma,color='black', linestyle='-',
#  label="RWsigma")


#axes.plot(thetaExp,RWpiExp,color='black', marker='x', linestyle='--', markersize=5, label="experimental")
axes.scatter(thetaExp,RWpiExp,color='black', marker='x',label="RWpi_experimental")#, markersize=5)
  
  
axes.set_xlabel('delta')
axes.set_ylabel('relative weights')
axes.set_title('Angle dependent EELS hBN')
#axes.legend(loc="upper right")
plt.legend(loc=2)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.ticklabel_format(style='plain', axis='y', scilimits=(0,0))

plt.show()
fig.savefig('relBKall_v1', bbox_inches='tight')