import pandas as pd

df=pd.read_csv("Day4/students.csv")

#print(df.duplicated())
#print(df.drop_duplicates())
df.drop_duplicates().reset_index(drop=True)
#df.to_csv("students_result.csv",index=False)

#print(df.isnull())
#print(df.isnull().sum(axis=1))

#print(df.dropna())

#df.dropna(inplace=True)
#print(df)

#df["math"]=df["math"].fillna(0)
#mean_math=df["math"].mean()
#df["math"]=df["math"].fillna(mean_math)



print(df)