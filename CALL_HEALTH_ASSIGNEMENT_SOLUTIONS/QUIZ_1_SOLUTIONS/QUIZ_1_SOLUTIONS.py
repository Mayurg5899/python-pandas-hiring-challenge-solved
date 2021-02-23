
import pandas as pd


database_df=pd.read_csv("database_1.csv")  #reading database.csv file
output_df=pd.read_csv("missing_emails.csv") #reading output.csv file

def getMissingEmails(data):

    try:
        _id=data.get('id')
        email=data.get('email')
        if(pd.isna(email)):
            df=database_df[database_df['id']==_id].reset_index()
            email=df['email'][0]
            return email
        return email
    except Exception as e:
        print(e)

output_df['email']=output_df[['id','email']].apply(getMissingEmails,axis=1)

def create_excel(df):
    writer = pd.ExcelWriter(f'OUTPUT_MISSING_EMAILS.xlsx',engine='xlsxwriter')
    df.to_excel(writer, index=False)

    writer.save()
    print('DataFrame is written successfully to Excel File.')

create_excel(output_df)   #new xls file is created to save the output_df dataframe 

#output_df.head(60)