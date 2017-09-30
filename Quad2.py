import cmath
def quad(a,b,c):
 d=(b*b)-(4*a*c)
 return d                                      
 a=float(input())                                
 b=float(input())                               
 c=float(input())                               
 d=quad(a,b,c)
r1=(-b+cmath.sqrt(d))/(2*a)                    
r2=(-b-cmath.sqrt(d))/(2*a)
print('r1={0} and r2={1}'.format(r1,r2))
