import numpy as np
import pandas as pd
import sys 
sys.path.append('..')
from admin import dbconnect as db
import pickle as pl

open_file = open('model/obj/ready_to_deploy.pkl', "rb")
to_deploy = pl.load(open_file)
open_file.close()

for crypto in to_deploy:

    df = pd.read_csv('csv/'+crypto+'_Predictions.csv')
    df.rename(columns={'date': 'Date', 'pred': 'Price'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    df2 = df.drop(df.columns[0], axis=1)
    df2.to_csv('csv/p_'+crypto.lower()+'.csv')

    print(crypto+' Model Deployed!!!\n\n')

file_name = 'model/obj/deployed.pkl'
open_file = open(file_name, "wb")
pl.dump(to_deploy, open_file)
open_file.close()




