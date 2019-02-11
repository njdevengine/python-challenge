import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    totalmonths = 0
    total = 0
    array = []
    months = []
    change = []
    avgtotal = 0
    for row in csvreader:
        totalmonths+=1
        total = total + int(row[1])
        array.append(int(row[1]))
        months.append((row[0]))
    for n in range (0,totalmonths-1):
        change.append(array[n+1]-array[n])
    for n in range (0,totalmonths-1):
        avgtotal = avgtotal + change[n]
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months: " + str(totalmonths))
    print("Total: $" + str(total))
    print("Average Change: "+ str(round(avgtotal/(totalmonths-1),2)))
    print("Greatest Increase in Profits: "+(months[change.index(max(change))+1])+" ($"+str(max(change))+")")
    print("Greatest Decrease in Profits: "+(months[change.index(min(change))+1])+" ($"+str(min(change))+")")
    outputFile = open("PyBankOutput.txt", "w")
    outputFile.write("Financial Analysis \n")
    outputFile.write("---------------------------------- \n")
    outputFile.write("Total Months: " + str(totalmonths)+"\n")
    outputFile.write("Total: $" + str(total)+"\n")
    outputFile.write("Average Change: "+ str(round(avgtotal/(totalmonths-1),2))+"\n")
    outputFile.write("Greatest Increase in Profits: "+(months[change.index(max(change))+1])+" ($"+str(max(change))+") \n")
    outputFile.write("Greatest Decrease in Profits: "+(months[change.index(min(change))+1])+" ($"+str(min(change))+") \n")
    outputFile.close()
