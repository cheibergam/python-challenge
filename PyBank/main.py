import os
import csv

# File path based on the relative path
filepath = "./Resources/budget_data.csv"

# Opening CSV file
csvfile = open(filepath, 'r')
csvreader = csv.reader(csvfile, delimiter=',')

# Initialising the variables 
number_of_rows = 0
greatest_increase = ["", 0]  # Will be used to store the month and the greatest increase
greatest_decrease = ["", 0]  # Will be used to store the month and the greatest decrease
total_changes = 0            # Sum of the total changes from one month to another
total_profit_loss = 0        # Sum the total of profit/loss accross all the months in the dataset

# Header of the CSV file
header = next(csvreader)

for row in csvreader:    
    number_of_rows = number_of_rows + 1
    if number_of_rows != 1:  # First row has to skip the calculation of the changes (no previous row to compare)
        
        # Calculating the profit/loss change from the previous month when copared with the current month
        change = int(row[1]) - int(previous_row[1])
        total_changes = total_changes + change
        
        if change > greatest_increase[1]:       # Checking if the current change is BIGGER than all the previous
            greatest_increase[1] = change
            greatest_increase[0] = row[0]            
        else:
            if change < greatest_decrease[1]:   # Checking if the current change is LOWER than all the previous
                greatest_decrease[1] = change
                greatest_decrease[0] = row[0]
        
    total_profit_loss = total_profit_loss + int(row[1])
    
    # Reference to the previous row in the loop, to be used to compare greatest increase/decrease in the next iteration
    previous_row = row

average_changes = total_changes / (number_of_rows-1)

# Closing CSV file
csvfile.close()

# Writing the results TXT file in the analysis folder
with open('./analysis/results.txt', 'w') as f:
    f.write ("Financial Analysis\n")
    f.write ("----------------------------\n")
    f.write ("Total Months: " + str(number_of_rows) + "\n")
    f.write ("Total: $" + str(total_profit_loss) + "\n")
    f.write ("Average Change: $" + str(round(average_changes,2)) + "\n")
    f.write ("Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")\n")
    f.write ("Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")")
    f.close()

# Printing the report in the screen
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(number_of_rows))
print ("Total: $" + str(total_profit_loss))
print ("Average Change: $" + str(round(average_changes,2)))
print ("Greatest Increase in Profits: " + greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")")
print ("Greatest Decrease in Profits: " + greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")")