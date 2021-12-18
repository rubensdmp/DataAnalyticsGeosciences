import pandas as pd
import probscale
import seaborn as sn
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
    args.add_argument("--cont", nargs="*", type=str,default=['bo', 'py', 'cpy'])
    args.add_argument("--cat", nargs="*", type=str,default=['ug'])
    return args.parse_args()


def main(args):
    DH = pd.read_csv(args.filename, sep=',')
    continuous = args.cont
    geology = args.cat[0]
    corrMatrix = DH[continuous].corr()
    
    #HEATMAP
    sn.heatmap(corrMatrix, annot=True)
    plt.savefig('corrMatrix{}.png'.format(continuous))
    plt.close()

    #SCATTER
    if len(continuous) > 2:
        cols = 2
        UGs = DH.groupby(geology).groups.keys()
        rows = int(len(DH.groupby(geology).groups.keys())/cols) + 1
        fig, axes = plt.subplots(rows, cols, constrained_layout=True, figsize=(10,10))
        for index, ug in enumerate(UGs):
            DH.groupby(geology).get_group(ug).plot.scatter(x=continuous[0], y=continuous[1], title=str(ug), ax=axes[int(index/cols), index%cols])
            axes[int(index/cols), index%cols].set_xlim((-0.1, 2.0))
            axes[int(index/cols), index%cols].set_ylim((-0.5, 16.0))

        for index in range(cols*rows):
            if (index + 1) > len(UGs):
                fig.delaxes(axes[int(index/cols), index%cols])

        plt.savefig('scatter_by_ug.png')
        plt.close()

    #Media Condicional
    step = 120.0
    DH['Step_East'] = step*(DH[args.coord[0]]/step).astype(int) + step/2.0

    x = DH.groupby('Step_East').groups.keys()
    y = DH.groupby('Step_East').describe()[args.coord[0]]['count'].values
    plt.plot(list(x), y)
    plt.title('Cantidad de muestras agrupadas por vista East (step=120)')
    plt.savefig('Step_East.png')
    plt.close()

    if len(continuous) >= 2:
        #Media Condicional
        groupby = DH.groupby('Step_East')
        fig, ax1 = plt.subplots(figsize=(10,10))
        ax1.set_xlabel(args.coord[0])
        ax1.plot(list(groupby.groups.keys()), groupby.describe()[continuous[0]]['mean'], color='tab:red')
        ax1.set_ylabel(continuous[0], color='tab:red')
        ax2 = ax1.twinx()
        ax2.plot(list(groupby.groups.keys()), groupby.describe()[continuous[1]]['mean'],color='tab:blue')
        ax2.set_ylabel(continuous[1], color='tab:blue')
        plt.title('Media Condicional')
        plt.savefig('East.png')
        plt.close()

        #3D
        fig = px.scatter_3d(DH, x=args.coord[0], y=args.coord[1], z=args.coord[2], color=continuous[0], color_continuous_scale=px.colors.sequential.Jet, range_color=[0.0, DH[continuous[0]].quantile(0.95)])
        fig.update_traces(marker=dict(size=5.0))
        fig.write_html('{}.html'.format(continuous[0]), auto_open=True)
        fig = px.scatter_3d(DH, x=args.coord[0], y=args.coord[1], z=args.coord[2], color=continuous[1], color_continuous_scale=px.colors.sequential.Jet, range_color=[0.0, DH[continuous[1]].quantile(0.95)])
        fig.update_traces(marker=dict(size=5.0))
        fig.write_html('{}.html'.format(continuous[1]), auto_open=True)
        
        #Probplot
        fig, ax = plt.subplots(figsize=(10,10))
        for ug in DH.groupby(geology).groups.keys():
            xData = DH.groupby(geology).get_group(ug)[continuous[0]].sort_values()
            probscale.probplot(xData, ax=ax, probax='y', datascale='log', label=ug)
        ax.legend()
        ax.set_ylim(bottom=0.001,top=99.99)
        ax.set_xlim(left=1e-4)
        plt.gca().xaxis.set_major_formatter(ScalarFormatter())
        ax.set_xlabel('Ordered Values')
        ax.set_ylabel('Normal probability scale (%)')
        ax.set_title('Probability Plot')
        plt.savefig('probability_plot_{}_{}.png'.format(continuous[0], geology))
        plt.close()

        #Probplot
        fig, ax = plt.subplots(figsize=(10,10))
        for ug in DH.groupby(geology).groups.keys():
            xData = DH.groupby(geology).get_group(ug)[continuous[1]].sort_values()
            probscale.probplot(xData, ax=ax, probax='y', datascale='log', label=ug)
        ax.legend()
        ax.set_ylim(bottom=0.001,top=99.99)
        ax.set_xlim(left=1e-4)
        plt.gca().xaxis.set_major_formatter(ScalarFormatter())
        ax.set_xlabel('Ordered Values')
        ax.set_ylabel('Normal probability scale (%)')
        ax.set_title('Probability Plot')
        plt.savefig('probability_plot_{}_{}.png'.format(continuous[1], geology))
        plt.close()
    
    DH.to_csv('output_mod6.csv', index=False)
  
    
if __name__ == "__main__":  
    args = set_params()
    print('filename', args.filename)
    print('coords', args.coord)
    print('continuous', args.cont)
    print('categorical', args.cat)
    main(args)