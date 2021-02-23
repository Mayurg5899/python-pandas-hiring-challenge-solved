import pandas as pd

studentsMarks_df=pd.read_csv('student_scores.csv')

def getMarkStandarize(marks):
    try:
        if(marks <= 78):
            return "failed"
        
        elif(78 < marks <= 85):
            return "passed"
        
        elif(marks>85):
            return "merit"
        
    except Exception as e:
        print(e)

studentsMarks_df['tag']=studentsMarks_df['marks'].apply(getMarkStandarize)

def create_excel(df):
    writer = pd.ExcelWriter(f'EXAMPLE_OUTPUT_STANDARIZE_MARKS.xlsx',engine='xlsxwriter')
    df.to_excel(writer, index=False)

    writer.save()
    print('DataFrame is written successfully to Excel File.')

create_excel(studentsMarks_df)

#APPLIED directly function on marks as i have checked the dtypes and found marks was in float so can get the standarization qucikly in this way
#studentMarks_df.dtypes to check dtypes