import pandas as pd
import matplotlib.pyplot as plt

#creates menu of options
def option(num):
    #outputs the first 5 rows of the csv file
    if num == 1:
        item5 = df.head()
        print(item5)
    #outputs the sum of all columns
    if num == 2:
        df_sum = df.sum()
        print(df_sum)
    #outputs the cumulative sum of all columns
    if num == 3:
        df_cumsum = df.cumsum()
        print(df_cumsum)
    #outputs the maximum value of all columns
    if num == 4:
        df_max = df.max()
        print(df_max)
    #outputs the minimum value of all columns
    if num == 5:
        df_min = df.min()
        print(df_min)
    #outputs the mean value of a column
    if num == 6:
        print(df.columns)
        col = str(input("What column do you want the mean of? "))
        print(df[col])
        mean = df[col].mean()
        print(mean)
    #outputs the median value of a column
    if num == 7:
        print(df.columns)
        col = str(input("What column do you want the median of? "))
        print(df[col])
        median = df[col].median()
        print(median)
    #outputs the ascending order of the users selected column's data
    if num == 8:
        print(df.columns)
        col = str(input("What column do you want the ascending order of? "))
        asc_order = df.sort_values(col, ascending=True)
        print(asc_order)
    #outputs the descending order of the users selected column's data
    if num == 9:
        print(df.columns)
        col = str(input("What column do you want the descending order of? "))
        desc_order = df.sort_values(col, ascending=False)
        print(desc_order)
    #outputs the data frame pivot of the users selected columns
    if num == 10:
        print(df.columns)
        col = str(input("What column do you want the dataframe pivot of? "))
        val = str(input("What column do you want the dataframe pivot values of? "))
        pivot = df.pivot(columns=col, values=[val])
        print(pivot)
    #outputs the data frame types
    if num == 11:
        types = df.dtypes
        print(types)
    #outputs the data frame shape
    if num == 12:
        shape = df.shape
        print(shape)
    #outputs the data frame info
    if num == 13:
        info = df.info()
        print(info)
    #outputs the data frame describe
    if num == 14:
        describe = df.describe()
        print(describe)
    #outputs the data frame visualisation of the users selected columns
    if num == 15:
        print(df.columns)
        col = str(input("What column do you want to be in the x-axis of the graph? "))
        val = str(input("What column do you want to be in the y-axis of the graph? "))
        x = df[col]
        y = df[val]
        plt.scatter(x,y)
        plt.show()

    elif num not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        print("Option does not exist, would you like to try again? ")
        ch = input("[y/n]? ")
        if ch.lower() == "y":
            return option(num)
    else:
        return 
        
df = pd.read_csv("sample.csv")
print("Options:")
print("1. View 1st 5 rows of dataset")
print("2. Sum of Values")
print("3. Cumulative Sum of Values")
print("4. Maximum Value")
print("5. Minimum Value")
print("6. Mean of Values in a column")
print("7. Median of Values in a column")
print("8. Sort Data in Ascending Order")
print("9. Sort Data in Descending Order")
print("10. Data Frame Pivot")
print("11. Data Frame Types")
print("12. Data Frame Shape")
print("13. Data Frame Info")
print("14. Data Frame Describe")
print("15. Data Frame Visualisation")
ch="y"
while ch.lower() == "y":
    num=int(input("What option do you choose? "))
    option(num)
    ch=input("Do you want to continue or not? [y/n] ")