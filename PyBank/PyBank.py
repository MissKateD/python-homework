# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:38:40 2021

@author: kd_84
"""
# Financial Analysis
from pathlib import Path
import csv

csvpath = Path('C:/Users/kd_84/Homework/python-homework/PyBank/budget_data.csv')
total_months = 0
total_net = 0
greatest_increase = 0
greatest_decrease = 0

with open(csvpath) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
 
        current_change = int(row[1])
        if current_change > greatest_increase:
            greatest_increase = current_change
        
    
        if current_change < greatest_decrease:
            greatest_decrease = current_change



average_change = round(total_net / total_months)

print('total_months = ', total_months)
print('total_net = ', total_net)
print('greatest_increase = ', greatest_increase)
print('greatest_decrease = ', greatest_decrease) 
print('average_change = ', average_change)