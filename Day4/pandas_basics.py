import pandas as pd
data={
    "name":["Tom","Jock","Alice","Bob","Lucy"],
    "math":[90,78,96,85,92],
    "english":[85,92,88,76,95]
}

df=pd.DataFrame(data)
#print(df.sort_values("math"))
#print(df.sort_values("math",ascending=False))
df["total"]=df["math"]+df["english"]
df["average"]=df["total"]/2
#df=df.drop(columns=["average"])
df.drop(columns=["average"],inplace=True)
#df.loc[3,"math"]=88
#df.loc[df["name"]=="Bob","math"]=88
#print(df.loc[1:3,["name","math"]])
#print(df.loc[2, "math"])
#print(df.iloc[2, 1])
#print(df.iloc[0])
#print(df[(df["math"]>=90)&(df["english"]>=90)])
#print(df[df["math"]>=90])
#print(df[["name","math"]])
#print(df["math"])
print(df)
#print(df.head(3))
#df.info()
#print(df.describe())