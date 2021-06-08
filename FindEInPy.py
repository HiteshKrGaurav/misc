print("Hello World!")

# Inputs
R = float(input("R = "))
x = float(input("x = "))
Q = float(input("Q = "))

# Constants
k = (9*(10**9))
E = ((k*Q*x)/(((R**2)+(x**2))**(3/2)))

# Scientific Notation

E1 = E
E2 = 0

while(E1 > 10):
    E1 = E1/10
    E2 = E2 + 1

# Result
# print(f"The magnitude of Electric Field is {E}")
print(f"\nE = {E1} x 10^{E2}")
