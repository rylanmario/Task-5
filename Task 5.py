# Name: Task 5.py
# Author: Rylan Fessey
# Date created: October 29th, 2022
# Date last modified: October 29th, 2022
# Purpose: The purpose of this program is to take numbers from 1-10 and cubes them.

cubednumbers = {}
for i in range(1,11):
    cubednumbers[i] = i*i*i
print(cubednumbers)