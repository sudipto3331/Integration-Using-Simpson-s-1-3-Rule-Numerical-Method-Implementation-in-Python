"""
Solve for X^2+5*X-9
"""
def F(x):
    return x*x

def Simpsons_13_interpolation(a,b,n):
    h=(b-a)/n
    integration=0
    for i in range(n):
        x0=a+i*h
        x1=x0+h/2
        x2=a+(i+1)*h
        val=h*(F(x0)+4*F(x1)+F(x2))/6
        integration=integration+val
    return integration

print("____Simpson's 1/3 Rule____")
a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
step_size=int(input("Eter the number of segment: "))
integration=Simpsons_13_interpolation(a, b,step_size)
print("\nIntregrated value = %.6f"%(integration))
