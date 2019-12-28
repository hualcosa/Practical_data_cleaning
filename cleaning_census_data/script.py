#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This was a project i developed during the course "Practical data cleaning" i've 
taken at Codecademy.

Project description:
You just got hired as a Data Analyst at the Census Bureau, which collects
census data and creates interesting visualizations and insights from it.

The person who had your job before you left you all the data they had for the
most recent census. It is in multiple csv files. They didn’t use pandas, they
would just look through these csv files manually whenever they wanted to find
something. Sometimes they would copy and paste certain numbers into Excel to
make charts.

The thought of it makes you shiver. This is not scalable or repeatable.

Your boss wants you to make some scatterplots and histograms by the end of the
day. Can you get this data into pandas and into reasonable shape so that you
can make these histograms?
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import glob

'''

It will be easier to inspect this data once we have it in a DataFrame. You
can’t even call .head() on these csvs! How are you supposed to read them?

Using glob, loop through the census files available and load them into
 DataFrames. Then, concatenate all of those DataFrames together into one
 DataFrame, called something like us_census.
'''
filenames = glob.glob("states*.csv")
df_list = []
for filename in filenames:
    data = pd.read_csv(filename)
    df_list.append(data)
us_census = pd.concat(df_list)

'''
Look at the .columns and the .dtypes of the us_census DataFrame. Are those
datatypes going to hinder you as you try to make histograms?
'''
#print(us_census.head())
#print(us_census.dtypes)

'''
Use regex to turn the Income column into a format that is ready for conversion
into a numerical type.
'''
us_census.Income = us_census.Income.replace('\$', '', regex=True)
us_census.Income = pd.to_numeric(us_census.Income)
#to confirm that the data type was altered:
#print(us_census.dtypes)

'''
Look at the PopulationGender column. We are going to want to separate this into
two columns, the Men column, and the Women column.

Split the column into those two new columns using str.split and separating out 
those results.
'''
genderPop_split = us_census.GenderPop.str.split('_')
us_census['Men'] = genderPop_split.str.get(0)
us_census.Men = us_census['Men'].replace('M', '', regex=True)
us_census.Men = pd.to_numeric(us_census['Men'])
us_census['Women'] = genderPop_split.str.get(1)
us_census['Women'] = us_census['Women'].replace('F', '', regex=True)
us_census.Women =pd.to_numeric(us_census['Women'])

#filling the missing values
us_census = us_census.fillna(value={'Women':us_census.TotalPop - us_census.Men})


'''
Removing the duplicates
'''
#if you to check if there are duplicates:
#print(us_census.duplicated())
us_census = us_census.drop_duplicates()

'''
Now you should have the columns you need to make the graph and make sure your
boss does not slam a ruler angrily on your desk because you’ve wasted your
whole day cleaning your data with no results to show!
'''
plt.scatter(us_census['Women'], us_census['Income'])
plt.title('Income vs number of Women per state')
plt.xlabel('Amount of Women per State')
plt.ylabel('Dollars')
plt.show()


'''
.
Now, your boss wants you to make a bunch of histograms out of the race data
that you have. Try to make a histogram for each one
'''
us_census.Hispanic = us_census['Hispanic'].replace('%','', regex=True)
us_census.White = us_census['White'].replace('%','', regex=True)
us_census.Black = us_census['Black'].replace('%','', regex=True)
us_census.Native = us_census['Native'].replace('%','', regex=True)
us_census.Asian = us_census['Asian'].replace('%','', regex=True)
us_census.Pacific = us_census['Pacific'].replace('%','', regex=True)

us_census.Hispanic = pd.to_numeric(us_census.Hispanic)
us_census.White = pd.to_numeric(us_census.White)
us_census.Black = pd.to_numeric(us_census.Black)
us_census.Native = pd.to_numeric(us_census.Native)
us_census.Asian = pd.to_numeric(us_census.Asian)
us_census.Pacific = pd.to_numeric(us_census.Pacific)

# making sure there is no Duplicates left
us_census = us_census.drop_duplicates()

plt.hist(us_census['Hispanic'])
plt.title('Hispanic Population Percentages distribution among States')
#plt.show()

plt.hist(us_census['White'])
plt.title('White Population Percentages distribution among States')
plt.show()

plt.hist(us_census['Black'])
plt.title('Black Population Percentages distribution among States')
plt.show()

plt.hist(us_census['Native'])
plt.title('Native Population Percentages distribution among States')
plt.show()

plt.hist(us_census['Asian'])
plt.title('Asian Population Percentages distribution among States')
plt.show()

plt.hist(us_census['Pacific'])
plt.title('Pacific Population Percentages distribution among States')
plt.show()



