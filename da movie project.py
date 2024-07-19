import pandas as pd

def option(num):
    if num == 1:
        df = pd.DataFrame(movieDataset)
        print(df)
    if num == 2:
        types = df.dtypes
        print(types)
    if num == 3:
        shape = df.shape
        print(shape)
    if num == 4:
        info = df.info()
        print(info)
    if num == 5:
        asc_order = df.sort_values("ratings", ascending=True)
        print(asc_order)
    if num == 6:
        desc_order = df.sort_values("ratings", ascending=False)
        print(desc_order)
    if num == 7:
        pivot = df.pivot(columns="movies", values=["ratings"])
        print(pivot)
    if num == 8:
        describe = df.describe()
        print(describe)
    elif num not in [1,2,3,4,5,6,7,8]:
        print("Option does not exist, would you like to try again?")
        ch = input("[y/n]?")
        if ch.lower() == "y":
            return option(num)
    else:
        return 
        

movieDataset = {
    "movies" : ["Avatar", "Batman"],
    "ratings" : [7,10]
    }

print("Options:")
print("1. Data Frame")
print("2. Data Types")
print("3. Data Shape")
print("4. Data Info")
print("5. Sort Data in Ascending Order")
print("6. Sort Data in Descending Order")
print("7. Data Pivot")
print("8. Data Describe")
ch="y"
while ch.lower() == "y":
    num=int(input("What option do you choose?"))
    option(num)
    ch=input("Do you want to continue or not?")



"""df = pd.DataFrame(movieDataset)
types = df.dtypes
shape = df.shape
info = df.info()
asc_order = df.sort_values("ratings", ascending=True)
desc_order = df.sort_values("ratings", ascending=False)
pivot = df.pivot(columns="movies",
values=["ratings"])
describe = df.describe()


print(df)
print(types)
print(shape)
print(info)
print(asc_order)
print(desc_order)
print(pivot)
print(describe)"""
                
