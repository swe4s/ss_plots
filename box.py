import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
import plot_lib

def main():
    args = plot_lib.get_args('Make a simple box plot.')

    names = []
    V = []
    i = 0
    for l in open(args.in_file):
        A = l.rstrip().split()
        names.append(A[0])
        V.append([float(v) for v in A[1:]])

    fig = plt.figure(figsize=(args.width,args.height),dpi=300)

    ax = fig.add_subplot(1,1,1)

    ax.boxplot(V)

    ax.set_xticklabels(names)

    ax.set_xlabel(args.x_label)
    ax.set_ylabel(args.y_label)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.savefig(args.out_file,bbox_inches='tight')

if __name__ == '__main__':
    main()
