import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
import plot_lib

def main():
    args = plot_lib.get_args('Make a simple histogram.')

    V = []
    for l in open(args.in_file):
        A = l.rstrip().split()
        V.append(float(A[0]))

    fig = plt.figure(figsize=(args.width,args.height),dpi=300)

    ax = fig.add_subplot(1,1,1)

    ax.hist(V)

    ax.set_xlabel(args.x_label)
    ax.set_ylabel(args.y_label)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.savefig(args.out_file,bbox_inches='tight')

if __name__ == '__main__':
    main()
