#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:52 2024

@author: user
"""

"""
Storing data in Python:
    
    1.Lists
    2. Dictionaries
    3. data frame - specific to pandas

"""


###############################
#
#   Lists
# 
###############################

import pandas as pd

file = pd.read_csv("country_data.csv")

print(file)

age1 = 30
age2 = 25
age3 = 40

age = [30,25,40]

print(age)

age_dat = file["Age"]

print(age_dat)


print(min(age_dat))
print(sum(age_dat))

age_avg = sum(age_dat)/len(age_dat)

print(age_avg)

age.append(109)
print(age)


age.insert(3,50) #insert the value in a position name.insert(pos,int)
print(age)



###############################
#
#   dictonary
# 
###############################

"""

cat: 'a cute animal'

- unordered


"""

mammals = {"cat":'a cute animal', 'lion':'king of the jungle', 'elephant':'a gigantic herbivore'}

print(mammals['cat'])



###############################
#
#   dataframe
# 
###############################


"""

df = short for dataframe

"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    "fruits":fruits,
    "sizes":Size_nm
    }

df = pd.DataFrame(fruit_sizes)

print(df[df['sizes'] > 10]) #filter data larger than 10 in sizes

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices #add column to dataframe

df.drop(columns=["sizes"], inplace= True)





















