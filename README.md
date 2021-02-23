# python-pandas-hiring-challenge-solved
There is a company who has given this task of descriptive analytics to solve using python library for data wrangling and manipulation i.e. pandas and numpy.So,i tried to solve them with this approach.You can see it to learn more and write better and efficient code with python and pandas.
#########QUIZ--1---Fill_Missing_Data

Get emails from "database.csv" and fill the missing email values in email column of "missing_emails.csv" file.

Example: In a row of "missing.csv" file you can see the id 110209, where email is empty for this id, but actual email mapped to same id is in "database.csv" file which is aanji009@yahoo.co.in.

Output should be:
All missing emails in "missing_emails.csv" should be filled, reference file "database.csv"

Hints:
Common key is "id" in both files.
###################################################################################################3
#########QUIZ--2----standardize_Them

We have a database called "student_scores.csv", in column "marks" you can see actual marks of the students, standardize the results as per the below guidelines. Standard tags should be filled in "tag" column (you need to create a new column named as "tag" in "student_scores.csv" file)

1. If student marks are >85 , then tag that student as "merit"
2. If student marks are >78 or <85, then tag that student as "passed"
3. If student marks are <78 then tag that student as "failed"

Example:

In a row user x got 75 marks, in "tag" column of that row, mark that user as "failed".

Hint:

Use pandas with python to do this.

Check Example_Output.csv file for reference.
######################################################################################################
#########QUIZ--3-------Quiz3_Split_And_Find
We have a "database.csv" file, in "users10.txt" text file we have 10 usernames.

Task:

In "database.csv" you can see email address, for example kiran@gmail.com is a mail id in "database.csv", in "users10.txt" file you can see kiran, 
you need to get value "kiran@gmail.com" for key "kiran".

Result for username "kiran" should in this format -> {"kiran":"kiran@gmail.com"}

Final output should be an array of dicts for each username(key), email_id pair.


Hint:
Use python strings operations.

Check Example_Output.txt file for reference.
########################################################################################################
########QUIZ---4----GetNumberedMails_with_Regex
We have a "database.csv" file.

Task:

Create 2 new columns in this database file, names should be "NumericFound", "numbers"

Subtasks:

1. If any digits (0 to 9) found in any email, extract that number and copy that into the "numbers" column else fill that row with NA
2. If any digit found in any email id just label it as "1" else "0" in "NumericFound" column.

Hint:
Use regex and pandas.

Check Example_Output.csv file for reference.
##################################################################################################################
NOTE:----OUTPUT OF ALL PROBLEMS ARE INSIDE FOLDER NAMED CALL_HEALTH.../QUIZ1.. respectively.
