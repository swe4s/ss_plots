import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
import plot_lib

def main():
    args = plot_lib.get_args('Make a simple scatter plot.')

    names = []
    X = []
    Y = []
    i = 0
    for l in open(args.in_file):
        A = l.rstrip().split()
        if len(A) == 3:
            names.append(A[0])
            X.append(float(A[1]))
            Y.append(float(A[2]))
        if len(A) == 2:
            X.append(float(A[0]))
            Y.append(float(A[1]))
        elif len(A) == 1:
            X.append(float(i))
            Y.append(float(A[0]))
            i+=1

    fig = plt.figure(figsize=(args.width,args.height),dpi=300)

    ax = fig.add_subplot(1,1,1)

    ax.plot(X, Y, '.', ms=3, alpha=1)

    if len(names) > 0:
        for i in range(len(names)):
            ax.text(X[i],Y[i],names[i], fontsize=4)

    ax.set_xlabel(args.x_label)
    ax.set_ylabel(args.y_label)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.savefig(args.out_file,bbox_inches='tight')

if __name__ == '__main__':
    main()
