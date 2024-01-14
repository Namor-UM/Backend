import math


def perimeter(types, x1, x2):
    x1, x2 = float(x1), float(x2)
    if types == "side_n_angle":
        return 4 * x1
    return 4 * (math.sqrt((x1/2)**2 + (x2/2)**2))


def height(types, x1, x2):
    x1, x2 = float(x1), float(x2)
    if types == "side_n_angle":
        return x1 * math.sin(math.radians(x2))
    return (x1 * x2) / math.sqrt(x1**2 + x2**2)


def radius(types, x1, x2):
    x1, x2 = float(x1), float(x2)
    if types == "side_n_angle":
        return (x1 * math.sin(math.radians(x2))) / 2
    return (x1*x2) / (2 * math.sqrt(x1**2 + x2**2))


output_names = ["Периметр", "Высота", "Радиус вписанной окружности"]
output_funcs = [perimeter, height, radius]