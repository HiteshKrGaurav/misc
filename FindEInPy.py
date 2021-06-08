R = NULL
x = NULL

print("hello")

# Inputs
R = int(input("Enter radius of circle :"))
x = int(input("Enter distance of P from the centre of ring :"))
Q = int(input("Enter Charge of Ring :"))

# Constants
k = (9*(10**9))

E = (k*Q*x)/(((R**2)+(x**2)**(3/2))

print("The Magnitude of electric field is %d", E)
