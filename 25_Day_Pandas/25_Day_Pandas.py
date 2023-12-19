import pandas as pd
from urllib.request import urlretrieve

hacker_news_url = "https://raw.githubusercontent.com/arewadataScience/30-Days-of-Python/main/data/hacker_news.csv"
urlretrieve(hacker_news_url, 'hacker_news.csv')
hacker_news_df = pd.read_csv('hacker_news.csv')


last_five_rows = hacker_news_df.iloc[-5:]

# Print the last five rows
print(last_five_rows)
last_five_rows = hacker_news_df.tail(5)

# Print the last five rows
print(last_five_rows)

last_five_rows = hacker_news_df.iloc[-5:, :]

# Print the last five rows
print(last_five_rows)

# 1. Get the title column as pandas series
title_series = hacker_news_df['title']

# Print the resulting Series
print(title_series)


num_rows, num_columns = hacker_news_df.shape

# Print the number of rows and columns
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)


filtered_df = hacker_news_df[hacker_news_df['title'].str.contains('python', case=False)]

# Print the filtered DataFrame
print(filtered_df)

filtered_df = hacker_news_df[hacker_news_df['title'].str.contains('JavaScript', case=False)]

# Print the filtered DataFrame
print(filtered_df)


hacker_news_df.info()



"""
From the above data it indicates that the csv file or data has seven columns and 20099 number of rows. 
it has no null values in the numeric columns. it has three integer fields and four string data types fields. 
"""



hacker_news_df.describe()



"""
from the above table it can be seen that the number of counts is 20099.000000 is the number of entries in the data.
The mean, standard deviation of the numeric coulumns are also indicated. The minimum and maximum entries are also 
indicated. The 50% num_points indiates the is not uniformly distributed along the num_points being the mean is 50.296632,
the minimum is 1.000000	and maximum is 2553.000000. The data is skewed towards one region, as can be seen from 25% 
percentile, the 75% and the maximum value. The skewness in the distribution is even worst in the case of num_comments 
columns.

 """





















