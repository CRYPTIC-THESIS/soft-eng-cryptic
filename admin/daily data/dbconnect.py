import firebase_admin
import pandas as pd
from firebase_admin import firestore 
from firebase_admin import db
from datetime import date as dt

import os

# Fetch the service account key JSON file contents
data = os.path.abspath(os.path.dirname(__file__)) + "/cryptic-database-firebase-adminsdk-bv1yi-dfd68e9690.json"
cred = firebase_admin.credentials.Certificate(data)

# Initialize the app with a None auth variable, limiting the server's access
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cryptic-database-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def insert_trend_csv(tbl_name,csv_path):
    ref = db.reference(tbl_name,default_app)
    df = pd.read_csv(csv_path)
    for index, row in df.iterrows():
        users_ref = ref.child(str(index))
        users_ref.set({
            'date':row['date'],
            'btc':row['bitcoin'], 
            'eth':row['ethereum'], 
            'doge':row['dogecoin']
    
    })
    print(csv_path+" Successfully Imported")

def insert_crypto_csv(tbl_name,csv_path):
    ref = db.reference(tbl_name,default_app)
    df = pd.read_csv(csv_path)
    for index, row in df.iterrows():
        users_ref = ref.child(str(index))
        users_ref.set({
            'date':row['Date'],
            'price':row['Closing Price (USD)'], 
            'open':row['24h Open (USD)'], 
            'high':row['24h High (USD)'],
            'low':row['24h Low (USD)']
    })
    print(csv_path+" Successfully Imported")

def insert_realtime_data(tbl_name, df):
    ref = db.reference(tbl_name,default_app)
    ref.delete() # DELETE EXISTING
    
    ref = db.reference(tbl_name,default_app)
    for index, row in df.iterrows():
        users_ref = ref.child(str(index))
        users_ref.set({
            'timestamp':row['Timestamp'],
            'open': row['Open'],
            'high':row['High'], 
            'low':row['Low'], 
            'closing':row['Closing']
    
    })
    print(tbl_name+" Successfully Imported")

def get_data_table(tbl_name):
    ref = db.reference(tbl_name,default_app)
    data = ref.get()
    data = pd.DataFrame(data)
    return data

def update_trend(tbl_name,values):
    ref = db.reference(tbl_name,default_app)
    data = ref.get()
    last_idx = len(data)
    for index, row in values.iterrows():
        users_ref = ref.child(str(last_idx+index))
        users_ref.set({
            'date':row['Date'],
            'btc':row['bitcoin'], 
            'eth':row['ethereum'], 
            'doge':row['dogecoin']
    
    })
    updated(tbl_name)
    print("Successfully Added "+str(len(values))+ "rows to " + tbl_name)

def update_crypto(tbl_name,values):
    ref = db.reference(tbl_name,default_app)
    data = ref.get()
    last_idx = len(data)
    for i, row in values.iterrows():
        users_ref = ref.child(str(last_idx+i))
        users_ref.set({
                    'date':row['Date'],
                    'price':row['Price'], 
                    'open':row['Open'], 
                    'high':row['High'],
                    'low':row['Low']
            })
    updated(tbl_name)
    print("Successfully Added "+str(len(values))+ "rows to " + tbl_name)

def update_realtime(tbl_name,values):
    ref = db.reference(tbl_name,default_app)
    data = ref.get()
    last_idx = len(data)
    for i, row in values.iterrows():
        users_ref = ref.child(str(last_idx+i))
        users_ref.set({
                    'timestamp':row['Timestamp'],
                    'open':row['Open'], 
                    'high':row['High'],
                    'low':row['Low'],
                    'closing':row['Closing']
            })
    updated(tbl_name)
    print("Successfully Added "+str(len(values))+ "rows to " + tbl_name)

def updated(tbl_name):
    today = dt.today().strftime("%d-%m-%Y")
    ref = db.reference('A_Last_Updated',default_app)
    users_ref = ref.child(tbl_name)
    users_ref.set(today)

#insert_trend_csv('Twitter_Data','path of twitter data')
#insert_trend_csv('Reddit_Data','path of reddit data')
#insert_trend_csv('Google_Data','path of google trend data')
#insert_crypto_csv('Bitcoin_Data','BTC_USD_2014-11-04_2021-09-20-CoinDesk.csv')
#insert_crypto_csv('Ethereum_Data','ETH_USD_2016-12-17_2021-09-20-CoinDesk.csv')
#insert_crypto_csv('Dogecoin_Data','DOGE_USD_2019-02-28_2021-09-20-CoinDesk.csv')

#data = get_data_table('Twitter_Data')