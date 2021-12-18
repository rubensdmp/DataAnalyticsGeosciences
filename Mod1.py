import pandas as pd 

def main():
    DH = pd.read_csv('db_mineralogia.csv', sep=',')
    DH.to_csv("output_file.csv", index=False) 
    
    DH = pd.read_excel('db_mineralogia.xlsx')
    DH.to_excel("output_file.xlsx", index=False)
    
    
if __name__ == "__main__":  
    main()