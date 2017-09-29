import cmath
import math
def dis(b,a,c):
 d=(b*b-(4*a*c))
 return d                                      
 a=float(input())                              
 b=float(input())                               
 c=float(input())
d=dis(b,a,c)                                    
if(d==0):
 print('roots real and equal')
 print('r1=r2={0}'.format((-b)/(2*a)))

elif(d>0):
 print('roots are real and disrinct')
 print("r1={0} and r2={1}".format(((-b)+math.sqrt(d))/(2*a),((-b)-math.sqrt(d))/(2*a)))

else:
 print('roots are imaginary')
 r=-b/(2*a)
 i=(cmath.sqrt(d))/(2*a)
 print('r1={0}-{1}and r2={2}+{3}'.format(r,i,r,i))
