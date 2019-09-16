import pretty_print as pp



def calculate_cube(x):
    return x ** 3


def calculate_square(x):
    return x ** 2

def main():
    pp.simple_print(calculate_square(2))
    pp.pro_print(calculate_cube(4))

main()