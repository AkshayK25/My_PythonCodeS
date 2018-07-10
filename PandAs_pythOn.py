import pandas as pd

# creation of user_defined data frame
print("--------------------creation of user_defined data frame------------------------------------")
Data = {'Name': ['Akshay', 'Rahul', 'Saif', 'Zeeshan', 'Faisal', 'Atif'],
        'Age': ['21 yrs', '21 yrs', '22 yrs', '22 yrs', '21 yrs', '21 yrs'],
        'Email': ['abc@gmail.com', 'xyz@gmail.com', 'qwer@gmail.com', 'ghi@gmail.com',
                  'jkl@gmail.com', 'mno@gmail.com'],
        'Phone No': [7896542513, 3698524712, 1236589748, 5432132975, 6516687656, 2684865465]}

display = pd.DataFrame(Data)
print(display)


# Data Extraction and Manipulation from CSv_file
print("\n-------------------------Data Extraction and Manipulation from CSv_file------------------------------\n")
df = pd.read_csv('weather.csv')
print(df)
print("\n----------------------------------------------------------------------------\n")
print(df.head(5))
print("\n----------------------------------------------------------------------------\n")
print(df.head(10))
print("\n----------------------------------------------------------------------------\n")
print(df.tail(5))
print("\n-----------------------------Data_statistics-------------------------------\n")
print(df.values)
print("\n----------------------------------------------------------------------------\n")
print(df.loc[2:, "MinTemp"])   # 2nd column Data stats
print("\n----------------------------------------------------------------------------\n")
print(df[1:6])   # first 5 rows data extraction
print("\n----------------------------------------------------------------------------\n")
print(df['WindGustDir'].values)   # Data stats for WindGustDirection in the form Array
print("\n---------------------------------End of ProgrAM!!-------------------------------------------\n")
