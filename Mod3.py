import pandas as pd
import probscale
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import argparse
import warnings
warnings.simplefilter('ignore')

def set_params():
    args = argparse.ArgumentParser()
    args.add_argument("--filename",  type=str, default="db_mineralogia.csv")
    args.add_argument("--coord", nargs="*", type=str,default=['East', 'North', 'Elevation'])
    args.add_argument("--cont", nargs="*", type=str,default=['bo'])
    args.add_argument("--cat", nargs="*", type=str,default=['dom'])
    return args.parse_args()


def main(args):
    DH = pd.read_csv(args.filename, sep=',')

    for CONT in args.cont:
        print(CONT)
        for CAT in args.cat:
            stats= DH.groupby([CAT]).describe()
            print(stats[CONT])
            fig, ax = plt.subplots(figsize=(10,10))
            for category in DH.groupby(CAT).groups.keys():
                xData = DH.groupby(CAT).get_group(category)[CONT].sort_values()
                probscale.probplot(xData, ax=ax, probax='y', datascale='log', label=category)
            ax.legend()
            ax.set_ylim(bottom=0.001,top=99.99)
            ax.set_xlim(left=1e-4)
            plt.gca().xaxis.set_major_formatter(ScalarFormatter())
            ax.set_xlabel('Ordered Values')
            ax.set_ylabel('Normal probability scale (%)')
            ax.set_title('Probability Plot')
            plt.savefig('probPlot_{}_{}'.format(str(CONT), str(CAT)))
            plt.close()
    
    
if __name__ == "__main__":  
    args = set_params()
    print('filename', args.filename)
    print('coords', args.coord)
    print('continuous', args.cont)
    print('categorical', args.cat)
    main(args)