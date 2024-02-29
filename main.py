import pandas as pd

#Get dict1 data from Youtube.

dict1 = {
        'Name': ['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'],
        'Marks': [98, 89, 99, 87, 90, 83, 99],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female']
        }

df1 = pd.DataFrame(dict1)
df1.to_csv('member_data.csv')

#1. Display top 3
# print(df1.head(3))

#2. Display bottom 3
# print(df1.tail(3))

#3. Find shape of the Dataset (Number of rows & column)
# print(df1.shape)
# rows = df1.shape[0]
# columns = df1.shape[1]
# print(f"Number of rows: {rows}")
# print(f"Number of columns: {columns}")

#4. Get info about our Dataset (total number of rows, columns, dtypes, memory req)
# print(df1.info())

#5. Check null values in dataset
# print(df1.isnull().sum())

#6. Get overall statistic in Dataframe
# print(df1.describe())

#7. Find Unique Values from Gender Column
# print(df1["Gender"].unique())

#8. Find The number of Unique Values from gender column
# print(df1["Gender"].nunique())

#9. Display Count of Unique Values in Gender Column
# print(df1["Gender"].value_counts())

#10. Find total number of students having marks between 90 and 100(inclusive) using between method
# print(len(df1[(df1["Marks"] >= 90) & (df1["Marks"] <= 100)]))
# print(sum(df1["Marks"].between(90, 100)))

#11. Find average Marks
# print(df1["Marks"].mean())

#12. Apply Method
# def Testing(x):
#     return x/2
#
# print(df1["Marks"].apply(Testing))

#13. Map Function
# df1["Male_Female"] = df1["Gender"].map({"Male": "Laki2", "Female": "Perempuan"})
# print(df1)

#14. Drop the column
# df1.drop("Male_Female", axis=1)

#15. Print name of the columns
# print(df1.columns)

#16. Sort The dataframe as per marks column
# print(df1.sort_values(by="Marks", ascending=False))

#17. Display the name & marks of Female Students
# print(df1[["Name", "Marks"]][df1["Gender"] == "Female"])