import math

def validateInput(x, n):
    if not isinstance(x, (int, float)):
        raise ValueError("x must be a number")
    
    if not isinstance(n, int):
        raise ValueError("n must be an integer")

    if n < 0:
        raise ValueError("n must be a positive integer")

    return float(x), int(n)

def calculate_sin(x, n):
    try:
        x, n = validateInput(x, n)

        sin_x = 0
        for i in range(n):
            sin_x += (-1) ** i * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)

        print(sin_x)
    except Exception as e:
        print(e)


def calculate_cos(x, n):
    try:
        x, n = validateInput(x, n)

        cos_x = 0
        for i in range(n):
            cos_x += (-1) ** i * (x ** (2 * i)) / math.factorial(2 * i)
        
        print(cos_x)
    except Exception as e:
        print(e)


def calculate_sinh(x, n):
    try:
        x, n = validateInput(x, n)

        sinh_x = 0
        for i in range(n):
            sinh_x += x ** (2 * i + 1) / math.factorial(2 * i + 1)
        
        print(sinh_x)
    except Exception as e:
        print(e)


def calculate_cosh(x, n):
    try:
        x, n = validateInput(x, n)

        cosh_x = 0
        for i in range(n):
            cosh_x += x ** (2 * i) / math.factorial(2 * i)
        
        print(cosh_x)
    except Exception as e:
        print(e)
    
    
calculate_cos(3.14, 1)