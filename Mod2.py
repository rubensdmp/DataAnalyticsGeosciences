import pandas as pd
import numpy as np
import plotly.express as px

import argparse
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

def set_params():
    args = argparse.ArgumentParser()
    args.add_argument("--filename",  type=str, default="db_mineralogia.csv")
    args.add_argument("--coord", nargs="*", type=str,default=['East', 'North', 'Elevation'])
    args.add_argument("--cont", nargs="*", type=str,default=['bo'])
    args.add_argument("--cat", nargs="*", type=str,default=['dom'])
    return args.parse_args()


def main(args):
    DH = pd.read_csv(args.filename, sep=',')

    for column in args.cont:
        fig = px.scatter_3d(DH, x=args.coord[0], y=args.coord[1], z=args.coord[2], color=column, color_continuous_scale=px.colors.sequential.Jet, range_color=[0.0, DH[column].quantile(0.95)])
        fig.update_traces(marker=dict(size=5.0))
        fig.write_html(column + '.html', auto_open=True)

    for column in args.cat:
        DH[column] = DH[column].astype(str)
        fig = px.scatter_3d(DH, x=args.coord[0], y=args.coord[1], z=args.coord[2], color=column)
        fig.update_traces(marker=dict(size=5.0))
        fig.write_html(column + '.html', auto_open=True)

    for column in args.cont:
        DH[column][DH[column] <= 0] = np.nan
    
    stats = DH.describe().T
    
    stats['IQR'] = stats['75%'] - stats['25%']
    stats['95%'] = DH.quantile(0.95)

    print(stats)

    stats.to_csv('stats.csv')
    DH.to_csv('DH.csv', index=False)
    
    
if __name__ == "__main__":  
    args = set_params()
    print('filename', args.filename)
    print('coords', args.coord)
    print('continuous', args.cont)
    print('categorical', args.cat)
    main(args)