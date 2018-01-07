import pylab
import argparse

if __name__ == "__main__":
    pars = argparse.ArgumentParser()
    pars.add_argument("file")
    args = pars.parse_args()

    data = pylab.loadtxt(args.file)
    pylab.plot(data[:,0], data[:,1], label="just a plot")
    pylab.legend()
    pylab.title(args.file)
    pylab.xlabel("Number of Inputs")
    pylab.ylabel("Time to Completion [sec]")
    pylab.show()
