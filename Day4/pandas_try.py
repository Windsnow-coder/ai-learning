import pandas as pd
df=pd.read_csv("Day4/students_try.csv")
df=df.drop_duplicates().reset_index(drop=True)
print(df.isnull().sum())
df["math"]=df["math"].fillna(df["math"].mean())
df["total"]=df["math"]+df["english"]
df["average"]=df["total"]/2
df.sort_values("average",ascending=False,inplace=True)
df=df[df["average"]>=90]
df.to_csv("Day4/students_result.csv",index=False)