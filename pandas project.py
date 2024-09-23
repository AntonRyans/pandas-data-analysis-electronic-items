import pandas as pd

def option(num):
    if num == 1:
        item5 = df.head()
        print(item5)
    if num == 2:
        row1 = int(input("Starting row?"))
        row2 = int(input("Final row?"))
        col1 = int(input("Starting column?"))
        col2 = int(input("Final column?"))
        sel = item5.iloc([row1, row2], [col1, col2])
        print(sel)
    if num == 3:
        types = df.dtypes
        print(types)
    if num == 4:
        shape = df.shape
        print(shape)
    if num == 5:
        info = df.info()
        print(info)
    if num == 6:
        asc_order = df.sort_values("ratings", ascending=True)
        print(asc_order)
    if num == 7:
        desc_order = df.sort_values("ratings", ascending=False)
        print(desc_order)
    if num == 8:
        pivot = df.pivot(columns="movies", values=["ratings"])
        print(pivot)
    if num == 9:
        describe = df.describe()
        print(describe)
    if num == 10:
        df_sum = df.sum()
        print(df_sum)
    if num == 11:
        df_cumsum = df.cumsum()
        print(df_cumsum)
    if num == 12:
        df_max = df.max()
        print(df_max)
    if num == 13:
        df_min = df.min()
        print(df_min)
    if num == 14:
        mean = df.mean()
        print(mean)
    if num == 15:
        median = df.median()
        print(median)
    elif num not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        print("Option does not exist, would you like to try again?")
        ch = input("[y/n]?")
        if ch.lower() == "y":
            return option(num)
    else:
        return 
        
df = pd.read_csv("sample.csv")
print("Options:")
print("1. View 1st 5 rows of dataset")
print("2. View Selected rows and columns")
print("3. Data Frame Types")
print("4. Data Frame Shape")
print("5. Data Frame Info")
print("6. Sort Data in Ascending Order")
print("7. Sort Data in Descending Order")
print("8. Data Frame Pivot")
print("9. Data Frame Describe")
print("10. Sum of Values")
print("11. Cumulative Sum of Values")
print("12. Maximum Value")
print("13. Minimum Value")
print("14. Mean of Values")
print("15. Median of Values")
ch="y"
while ch.lower() == "y":
    num=int(input("What option do you choose?"))
    option(num)
    ch=input("Do you want to continue or not?")

