import pandas as pd
import probscale
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import argparse
import plotly.express as px
import warnings
warnings.simplefilter('ignore')


def set_params():
    args = argparse.ArgumentParser()
    args.add_argument("--filename",  type=str, default="output_mod4.csv")
    args.add_argument("--coord", nargs="*", type=str,default=['East', 'North', 'Elevation'])
    args.add_argument("--cont", nargs="*", type=str,default=['bo'])
    args.add_argument("--cat", nargs="*", type=str,default=['ug'])
    return args.parse_args()


def main(args):
    DH = pd.read_csv(args.filename, sep=',')
    continuous = args.cont[0]
    geology = args.cat[0]
    DH[geology] = DH[geology].astype(str)
    stats = DH.groupby([geology]).describe()
    print(stats[continuous])

    fig, ax = plt.subplots(figsize=(10,10))
    for ug in DH.groupby(geology).groups.keys():
        xData = DH.groupby(geology).get_group(ug)[continuous].sort_values()
        probscale.probplot(xData, ax=ax, probax='y', datascale='log', label=ug)
    ax.legend()
    ax.set_ylim(bottom=0.001,top=99.99)
    ax.set_xlim(left=1e-4)
    plt.gca().xaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlabel('Ordered Values')
    ax.set_ylabel('Normal probability scale (%)')
    ax.set_title('Probability Plot')
    plt.savefig('probability_plot_{}.png'.format(geology))
    plt.close()

    fig = px.scatter_3d(DH, x=args.coord[0], y=args.coord[1], z=args.coord[2], color=geology)
    fig.update_traces(marker=dict(size=5.0))
    fig.write_html(geology + '.html', auto_open=True)

    DH.hist(column=continuous, by=geology, figsize=(10,10))
    plt.savefig('hist_by_{}.png'.format(geology))
    plt.close()

    DH.boxplot(column=continuous, by=geology, figsize=(10,10))
    plt.yscale('log')
    plt.gca().yaxis.set_major_formatter(ScalarFormatter())
    plt.savefig('boxplot_by_{}.png'.format(geology))
    plt.close()

    fig, ax = plt.subplots()
    for ug in DH.groupby([geology]).groups.keys():
        ax.scatter(stats[continuous]['mean'][ug], stats[continuous]['std'][ug], label=ug)
    ax.legend()
    ax.set_xlabel('Median')
    ax.set_ylabel('Standard Deviation')
    ax.set_title('Median v/s Standard Deviation')
    plt.savefig('media_vs_std.png')
    plt.close()
    
if __name__ == "__main__":  
    args = set_params()
    print('filename', args.filename)
    print('coords', args.coord)
    print('continuous', args.cont)
    print('categorical', args.cat)
    main(args)