#Modules for reading csv files
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Setting global variables
profit_total = 0
num_months = 0
profit_change = 0
pl_max = 0
pl_min = 0
max_month = "10-Jan"
min_month = "10-Jan"
change_total = 0

#Method for reading csv files
with open(csvpath, 'r') as csvfile:

    #CSV reader identifies delimiter and variable that holds the contents
    csvreader = (csv.reader(csvfile, delimiter=','))
    next(csvreader)
    """Pull value of Profit/Loss column in the first row outside of 
    for loop so that you can have it to use as the first previous
    profit"""
    row1 = next(csvreader)
    profit_total = profit_total + (int(row1[1]))
    num_months = num_months + 1
    prev_profit = (int(row1[1]))
    """Run for loop define profit/loss total, number of months of data, profit change each month, 
    overall change total, and min and max profit/loss."""
    for row in csvreader:
        profit_total = profit_total + (int(row[1]))
        num_months = num_months + 1
        current_profit = (int(row[1]))
        profit_change = current_profit - prev_profit
        prev_profit = current_profit
        change_total = change_total + profit_change
        if profit_change > pl_max:
            pl_max = profit_change
            max_month = (str(row[0]))
        if profit_change < pl_min:
            pl_min = profit_change
            min_month = (str(row[0]))

#Calculate average change in profit for data set
average_change = round(change_total/(num_months - 1), 2)

#Create bank analysis report
lines = (
    
f"\nFinancial Analysis" 
f"---------------------------"
f"\n\nTotal Months:  {num_months}"
f"\n\nTotal:  $ {profit_total}"
f"\n\nAverage Change: $ {average_change}"
f"\n\nGreatest Increase in Profits:  {max_month} (${pl_max})"
f"\n\nGreatest Decrease in Profits:  {min_month} (${pl_min})\n"

)

#Print report to terminal
print(lines)

#Write report as output file.
# Specify the file to write to
output_path = os.path.join("Analysis", "bank_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as pl_analysis:
    pl_analysis.write(lines)


