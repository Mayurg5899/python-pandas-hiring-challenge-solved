import pandas as pd
import json
database_df=pd.read_csv("database.csv")
fh=open("users10.txt")
user_name=[line.strip() for line in fh]

def getlistofdic(email):
    try:
        newdic={}
        email_id=str(email).split('@')
        print(email_id)
        if(email_id[0] in user_name):
            newdic[email_id[0]]=email
            return newdic
    except Exception as e:
        print(e)
    
database_df['key-value']=database_df['email'].apply(getlistofdic)  
listofdic=list(database_df[database_df['key-value'].notnull()]['key-value'])
with open('output_file', 'w') as fout:
    json.dump(listofdic, fout)