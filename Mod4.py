import pandas as pd
import probscale
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import plotly.express as px
import warnings
warnings.simplefilter('ignore')

def main():
    filename = 'db_mineralogia.csv'
    DH = pd.read_csv(filename, sep=',')
    DH['ug'] = -99
    DH['ug'][(DH['dom'] != 3)] = 1
    DH['ug'][(DH['dom'] == 3)] = 2
    DH['ug'][(DH['ug'] == 2) & ((DH['alte'] == 'BTK') | (DH['alte'] == 'POT')) & (DH['mine'] != 'BN')] = 3
    DH['ug'][(DH['ug'] == 2) & ((DH['alte'] == 'BTK') | (DH['alte'] == 'POT')) & (DH['mine'] == 'BN')] = 4 
    stats = DH.groupby(['ug']).describe()
    print(stats['bo'])

    fig, ax = plt.subplots(figsize=(10,10))
    for category in DH.groupby('ug').groups.keys():
        xData = DH.groupby('ug').get_group(category)['bo'].sort_values()
        probscale.probplot(xData, ax=ax, probax='y', datascale='log', label=category)
    ax.legend()
    ax.set_ylim(bottom=0.001,top=99.99)
    ax.set_xlim(left=1e-4)
    plt.gca().xaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlabel('Ordered Values')
    ax.set_ylabel('Normal probability scale (%)')
    ax.set_title('Probability Plot')
    plt.savefig('probPlot_ug.png')
    plt.close()
    
    DH["ug"] = DH["ug"].astype(str)
    fig = px.scatter_3d(DH, x='East', y='North', z='Elevation', color='ug')
    fig.update_traces(marker=dict(size=5.0))
    fig.write_html('ug.html', auto_open=True)
    
    DH.to_csv('DH.csv',index=False)
    
    
if __name__ == "__main__":  
    main()