import os
import csv

# paths to files
csvpath = os.path.join("Resources","budget_data.csv")
csv_output = os.path.join("Analysis", "bank_analysis.txt")

# lists
total_months = 0

total_profit = 0

months_change = []

profit_change_list = []

great_increase = ["", 0]

great_decrease = ["", 9999999]


# open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)


    first_row = next(csvreader)
    total_months += 1
    total_profit += int(first_row[1])
    prev_total = int(first_row[1])

    for row in csvreader:

        total_months += 1 
        total_profit += int(first_row[1])
        
        profit_change = int(row[1]) - prev_total
        prev_total = int(row[1])
        profit_change_list += [profit_change]
        months_change += [row[0]]

        if profit_change > great_increase[1]:
            great_increase[0] = row[0]
            great_increase[1] = profit_change

        if profit_change < great_decrease[1]:
            great_decrease[0] = row[0]
            great_decrease[1] = profit_change

        


profit_avg = sum(profit_change_list) / len(profit_change_list)

output = (
    f"Financial Analysis\n"
    f"________________________\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f'Average Change: ${profit_avg: .2f}\n'
    f'Greatest Increase in Profit: {great_increase[0]} (${great_increase[1]})\n'
    f'Greatest Decrease in Profit: {great_decrease[0]} (${great_decrease[1]})\n')
print(output)

with open(csv_output, "w") as txt_file:
    txt_file.write(output)