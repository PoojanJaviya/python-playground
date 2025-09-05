import pandas as pd


#Creation of DataFrame
data = {
    "Name" : ["Messi","Ronaldo","Neymar","Modric","Benzema"],
    "Age" : [38,40,36,38,35],
    "Ballon d'or" : [8,5,0,1,1] 
} 

df = pd.DataFrame(data)
print(df)
print("\n")

#Accessing Columns and rows
print(df["Name"])
print("\n")
print(df[["Name","Ballon d'or"]])
print("\n")
print(df.loc[1])
print("\n")
print(df.iloc[1])
print("\n")


#filtering
print(df[df["Ballon d'or"] < 2])
print("\n")
print(df[df["Age"] > 35])
print("\n")
print(df[(df["Age"] > 35) & (df["Ballon d'or"] < 2)])
print('\n')

#Sorting
df.sort_values("Age",inplace=True)
print(df)
print("\n")
df.sort_values("Ballon d'or",ascending=False, inplace=True)
print(df)
print("\n")


#Adding/Dropping Columns
df["Goat"] = df["Ballon d'or"] > 4
print(df)
print("\n")
df.drop("Goat",axis=1,inplace=True)
print(df)
print("\n")


#reseting index 
df.reset_index(drop=True,inplace=True)
print(df)
