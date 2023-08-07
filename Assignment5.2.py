import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "Complex roots"

def main():
    print("Quadratic Equation Solver")
    print("-------------------------")
    
    # Input coefficients of the quadratic equation
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Call the function to solve the quadratic equation
    solutions = solve_quadratic(a, b, c)
    
    # Display the solutions
    print("Solutions:")
    if isinstance(solutions, tuple):
        root1, root2 = solutions
        print("Root 1:", root1)
        print("Root 2:", root2)
    else:
        print(solutions)

if __name__ == "__main__":
    main()
