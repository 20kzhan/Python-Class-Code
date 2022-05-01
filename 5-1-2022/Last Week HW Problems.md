Problem 1:
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
 
Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:
Input: date = "2019-02-10"
Output: 41


Problem 2:
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
 
day = 31, month = 8, year = 2019
"Saturday"
 

day = 18, month = 7, year = 1999
"Sunday"
 

day = 15, month = 8, year = 1993
"Sunday"


Problem 3:
You are given a positive integer num consisting only of digits 6 and 9.
Return 6996.
 
num = 9669
9969

Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

num = 9996
9999
Changing the last digit 6 to 9 results in the maximum number.
 

num = 9999
9999
It is better not to apply any change.
