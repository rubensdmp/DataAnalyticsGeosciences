import pandas as pd
import matplotlib.pyplot as plt
import argparse


def set_params():
    args = argparse.ArgumentParser()
    args.add_argument("--filename",  type=str, default="output_mod6.csv")
    return args.parse_args()


def main(args):
    DH = pd.read_csv(args.filename, sep=',')
    DH.to_csv('output.csv', index=False)
    print(DH.describe().T)
    DH.describe().T.to_csv('stats.csv')
    DH['bo'].hist(bins=20)
    plt.savefig('hist.png')
    plt.savefig('hist.jpg')
    plt.close()
    
if __name__ == "__main__":  
    args = set_params()
    print('filename', args.filename)
    main(args)