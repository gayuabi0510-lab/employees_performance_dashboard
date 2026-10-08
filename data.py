import pandas as pd
df=pd.read_csv("IT_employee_dataset.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.isnull().sum())
print(df[df.duplicated()])
df=df.drop_duplicates(subset="Employee_ID",keep="first")
print(df.shape)
df["Tasks_Completed"]=df["Tasks_Completed"].astype(int)

numeric_cols=["Experience_Years","Projects_Completed","Hours_Worked_Per_Week","Attendance_Percent","Performance_Rating","Productivity_Score","Monthly_Salary"]
for col in numeric_cols:
    median_val=df[col].median()
    df[col]=df[col].fillna(median_val)
df["Experience_Years"]=df["Experience_Years"].round(1)
df["Projects_Completed"]=df["Projects_Completed"].round(0).astype(int)
df["Hours_Worked_Per_Week"]=df["Hours_Worked_Per_Week"].round(1)
df["Attendance_Percent"]=df["Attendance_Percent"].round(1)
df["Performance_Rating"]=df["Performance_Rating"].round(0).astype(int)
bad = (df["Productivity_Score"] < 0) | (df["Productivity_Score"] > 100)
print("productivity rows outside 0-100:", bad.sum())
valid_median = df.loc[~bad, "Productivity_Score"].median()
df.loc[bad, "Productivity_Score"] = valid_median
df["Productivity_Score"]=df["Productivity_Score"].round(1)
print("Productivity range:", df["Productivity_Score"].min(), "-", df["Productivity_Score"].max())
df["Monthly_Salary"]=df["Monthly_Salary"].round(0).astype(int)
print(df.isnull().sum())
print(df.shape)
print(df.dtypes)
# remove rows with invalid rating or attendance
before = df.shape[0]
df = df[df["Performance_Rating"].between(1, 5) & df["Attendance_Percent"].between(0, 100)]
print("Removed invalid rows:", before - df.shape[0])
print("Rating range after fix:", df["Performance_Rating"].min(), "-", df["Performance_Rating"].max())
print("Attendance range after fix:", df["Attendance_Percent"].min(), "-", df["Attendance_Percent"].max())
print(df.shape)
df.to_csv("it_employees_data_cleaned.csv",index=False)
print("saved:it_employees_data_cleaned.csv")