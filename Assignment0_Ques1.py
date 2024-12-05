#problem 1
def slope_of_cubic(coefficient, x):
    a,b,c,d = coefficient
    slope = 3 * a * x**2 + 2 * b * x + c
    return slope
coefficient = (1,1,1,1)
print(slope_of_cubic(coefficient, 2))
