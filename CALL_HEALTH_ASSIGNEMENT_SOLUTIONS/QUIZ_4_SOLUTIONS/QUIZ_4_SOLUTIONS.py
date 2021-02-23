import pandas as pd
import json
import re
database_df=pd.read_csv("database.csv")
def getNumbers(email):
    try:
        pattern=r'[0-9]+'
        lst=re.findall(pattern, email) 
        if(len(lst)>0):
            return int(lst[0])
        return 'NA'
    except Exception as e:
        print(e)
database_df['numbers']=database_df['email'].apply(getNumbers)
database_df['numeric_found']=database_df['numbers'].apply(lambda x: 1 if not isinstance(x,str) else 0)
database_df=database_df[['email','numeric_found','numbers']]

def create_excel(df):
    writer = pd.ExcelWriter(f'EXAMPLE_OUTPUT_GetNumberedMails_with_Regex.xlsx',engine='xlsxwriter')
    df.to_excel(writer, index=False)

    writer.save()
    print('DataFrame is written successfully to Excel File.')

create_excel(database_df)
#database_df.head(40)