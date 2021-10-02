# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:38:40 2021

@author: kd_84
"""
# Financial Analysis

from pathlib import Path
import csv

csvpath = Path('C:/Users/kd_84/Homework/python-homework/PyBank/budget_data.csv')

Total_Months = []

Total = 0

with open(csvpath, 'r') as csvfile:
    
    print(type(csvfile))

    csvreader = csv.reader(csvfile, delimiter=',')
    print(type(csvreader))

for row in csvreader:
    print(row)

Total_Months= int(row[0])

Total_Months.append(Total_Months)

Total_Months = 0
Total = 0
Average_Change = 0
Greatest_Increase[Date, Total] = 0
Greatest_Decrease[Date, Time] = 0

with open("budget_data.csv")) as fin:
  headerline = fin.next()
  total = 0
  for row in csv.reader(fin):
  for col in row[1]:

total += int(col)
  print(Total)

    if min_Profit/Losses == 0:
        min_Profit/Losses = Profit/Losses
    elif Profit/Losses > max_Profit/Losses:
        max_Profit/Losses = Profit/Losses
    elif Profit/Losses < min_Profit/Losses:
        min_Profit/Losses = Profit_Losses

header = ["Financial Analysis"]

metrics = [Total_Months, Total, Average_Change, Greatest_Increase, Greatest_Decrease]

output_path = Path('budget_data.csv')

with open(output_path, 'w') as csvfile:

csvwriter = csv.writer(csvfile, delimiter=',')

csvwriter.writerow(header)

csvwriter.writerow(metrics)

header = next(csvreader)

    rows = 0
    total = 0
    Profit = 0
    Loss = 0
    row_profit = 0
    row_loss = 0
    Max = 0
    Min = 0

    PL_change = 0
    Total_PL_list = []
    Month_change = 0
    PL_change_list = []
    Total_months_list = []
    current_PL = 0
    last_PL = 0

for row in csvreader:
        rows += 1

        total = total + int(row[1])

        if (int(row[1]) > 0):
            Profit = Profit + int(row[1])
            row_profit += 1
        else:
            Loss = Loss + int(row[1])
            row_loss += 1


        Total_months_list.append(row[0])
        Total_PL_list.append(int(row[1]))


        if (int(row[1]) > Max):
            Max = int(row[1])
            Month_max = row[0]
        elif (int(row[1]) < Min):
            Min = int(row[1])
            Month_min = row[0]

for i in range(len(Total_PL_list) - 1):
        PL_change_list.append(Total_PL_list[i + 1] - Total_PL_list[i])

Average_change = (sum(PL_change_list)) / (len(PL_change_list))

    
print("Financial Analysis")
print("-----------------------\n")
print(f"Total Months: {str(rows)} \n")
print(f"Total: ${str(total)}\n")
print(f"Average Change: ${str('%.2f' % Average_change)}\n")
print(f"Greatest Increase in Profits: {Month_max} (${str(Max)})\n")
print(f"Greatest Decrease in Profits: {Month_min} (${str(Min)})\n")
