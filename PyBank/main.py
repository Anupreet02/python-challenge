import os 
import csv


#path to the csv file

csv_path= r"PyBank\Resources\budget_data.csv"

#set the variables
total_months = 0
net_total = 0
changes = []
dates = []
previous_profit_losses = None

#open and read the csv file
with open (csv_path)as csv_file:
    csvreader = csv.reader (csv_file,delimiter=",")
    #read the header row first
    csv_header= next(csvreader)

    #read through each row after header
    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])

        #to track the dates
        dates.append(date)
        #calculate the number of total months
        total_months +=1
        
        #calculate the net total amount
        net_total += profit_losses

        #calculate monthly change
        if previous_profit_losses is not None:
            change= profit_losses - previous_profit_losses
            changes.append(change)

        #update the previous profit losses
        previous_profit_losses = profit_losses
    
#calculate the average change
average_change = sum(changes)/len(changes) if changes else 0

#indentify the greatest increase and decrease 
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0
greatest_increase_date = dates[changes.index(greatest_increase) + 1] if changes else ''
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1] if changes else ''

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")