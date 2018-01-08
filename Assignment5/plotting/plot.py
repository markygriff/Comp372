import pylab
import argparse

if __name__ == "__main__":
    pars = argparse.ArgumentParser()
    pars.add_argument("file")
    args = pars.parse_args()

    data = pylab.loadtxt(args.file)
    pylab.plot(data[:,0], data[:,1])
    pylab.legend()
    pylab.title("Worst Case Input with First Fit")
    pylab.xlabel("Number of Inputs")
    pylab.ylabel("Time to Completion [sec]")
    pylab.show()
