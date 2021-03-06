
'''-------------------------------------------------------
-------------  All functions listed below  ---------------
----------------------------------------------------------'''
import math
#########################################
def my_quad_equation(coefa,coefb,coefc):
    if coefa and coefb and coefc != 0:
        equ=str("f(x)=%s*x**2+%s*x+%s"%(coefa,coefb,coefc)) ##for all positive a,b,c
    if coefa==1:
        equ=str("f(x)=x**2+%s*x+%s"%(coefb,coefc)) ##if a=1
    if coefa==-1:
        equ=str("f(x)=-x**2+%s*x+%s"%(coefb,coefc)) ##if a=-1
    if coefb==1:
        equ=str("f(x)=%s*x**2+x+%s"%(coefa,coefc)) ##if b=1
    if coefb==-1:
        equ=str("f(x)=%s*x**2-x+%s"%(coefa,coefc)) ##if b=-1
    if coefb==0:
        equ=str("f(x)=%s*x**2+%s"%(coefa,coefc)) ##if b=0
    if coefb<0:
        equ=str("f(x)=%s*x**2-%s*x+%s"%(coefa,abs(coefb),coefc)) #if b is negative
    if coefa and coefb==1:
        equ=str("f(x)=x**2+x+%s"%(coefc)) #if a and b are 1
    if coefa and coefb==-1:
        equ=str("f(x)=-x**2-x+%s"%(coefc)) #if a and b are -1
    if coefc==0:
        equ=str("f(x)=%s*x**2+%s*x"%(coefa,coefb))  #if c=0
    if coefc<0:
        equ=str("f(x)=%s*x**2+%s*x-%s"%(coefa,coefb,abs(coefc))) #if c is negative
    if coefb and coefc<0:
        equ=str("f(x)=%s*x**2-%s*x-%s"%(coefa,abs(coefb),abs(coefc))) #if b and c are negative
    return equ

##########################################


#########################################
def my_quad_equation_derivative(coefa,coefb):
    if coefb>0:
        dx="f'(x)="+str((coefa*2))+"*x+"+str(coefb) #if b is positive
    if coefb<0:
        dx="f'(x)="+str((coefa*2))+"*x-"+str(abs(coefb)) #if b is negative
    if coefb==0:
        dx="f'(x)="+str((coefa*2))+"*x" #if b is 0
    return dx

##########################################

##########################################
def info_extremum(coefa):
    if coefa>0:
        return "Minimum"
    else:
         return "Maximum" 
###########################################


############################################
def evaluate_quad_equation(coefa,coefb,coefc,x):
    x0=((coefb*-1)/(coefa*2))
    x=x0
    fx=(coefa*(x**2))+(coefb*x)+(coefc)
    return  fx
###########################################

#############################################
def compute_discriminant(coefa,coefb,coefc):
    delta=float((coefb**2)-(4*coefa*coefc))
    return delta
############################################


############################################
def print_info_solution_quad(coefa,coefb,coefc,delta):
    if delta>0:
        x1=float((-coefb+math.sqrt(delta))/(2*coefa))
        x2=float((-coefb-math.sqrt(delta))/(2*coefa))
        if x1<0:
            fact=("%s*(x+%s)(x-%s)"%(coefa,abs(x1),x2)) #if just solution 1 is negative
        if x2<0:
            fact=("%s*(x-%s)(x+%s)"%(coefa,x1,abs(x2))) #if just solution 2 is negative
        if x1<0 and x2<0:
            fact=("%s*(x+%s)(x+%s)"%(coefa,abs(x1),abs(x2))) #if solution 1&2 are negative
        if x1>0 and x2>0:
            fact=("%s*(x-%s)(x-%s)"%(coefa,x1,x2)) #if solution 1&2 are positive
        f=str("Two solutions:\t %s and %s\nFactorize form:\t%s"%(x1,x2,fact))
        return print(f)
    if delta==0:
        x1=x0
        if x1>0:
            fact=("%s*(x-%s)**2"%(coefa,x1)) #if solution is positive
        else:
            fact=("%s*(x+%s)**2"%(coefa,abs(x1)))
        f=str("One solution:\t %s\nFactorize form:\t%s"%(x1,fact)) #if solution is negative
        return print(f)
    if delta<0:
        x1=float(math.sqrt(abs(delta)))
        clex=("Two Complex Solutions:\t (%s-%sj) and (%s-%sj)"%(coefb/2*coefa,x1/2*coefa,coefb/2*coefa,x1/2*coefa)) ##complex solutions
        return print("No real solutions\n%s"%(clex))
##############################################


