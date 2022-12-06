from _sierpinski import Sierpinski

import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sideSize = 6
        iterations = 1000
    else:
        sideSize = float(sys.argv[1])
        iterations = int(sys.argv[2])

    sierpinski = Sierpinski(sideSize)
    sierpinski.generatePoints(iterations)
    sierpinski.plot()