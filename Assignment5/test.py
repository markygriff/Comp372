from first_fit import first_fit
from first_fit_decreasing import first_fit_decreasing

if __name__ == "__main__":
    objs = [0.5, 0.4, 0.35, 0.9, 0.7, 0.3, 0.1, 0.1, 0.5]
    first_fit(objs)
    first_fit_decreasing(objs)
