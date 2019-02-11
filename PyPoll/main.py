import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    totalvotes = 0
    khanvotes = 0
    correyvotes = 0
    livotes = 0
    tooleyvotes = 0
    for row in csvreader:
        totalvotes += 1
        if row[2] == "Khan":
            khanvotes += 1
        elif row[2] == "Correy":
            correyvotes += 1
        elif row[2] == "Li":
            livotes += 1
        else:
            tooleyvotes += 1
    print("Election Results")
    print("-------------------------------------")
    print("Total Votes: " + str(totalvotes))
    print("-------------------------------------")
    khan = round(((khanvotes / totalvotes) * 100), 3)
    correy = round(((correyvotes / totalvotes) * 100), 3)
    li = round(((livotes / totalvotes) * 100), 3)
    tool = round(((tooleyvotes / totalvotes) * 100), 3)
    print("Khan: " + str(khan) + "% (" + str(khanvotes) + ")")
    print("Correy: " + str(correy) + "% (" + str(correyvotes) + ")")
    print("Li: " + str(li) + "% (" + str(livotes) + ")")
    print("O'Tooley: " + str(tool) + "% (" + str(tooleyvotes) + ")")
    if max(khan, correy, li, tool) == khan:
        print("Winner: Khan")
    elif max(khan, correy, li, tool) == correy:
        print("Winner: Correy")
    elif max(khan, correy, li, tool) == li:
        print("Winner: Li")
    else:
        print("Winner: O'Tooley")

    outputFile = open("PyPollOutput.txt", "w")
    outputFile.write("Election Results \n")
    outputFile.write("---------------------------------- \n")
    outputFile.write("Total Votes: " + str(totalvotes) + "\n")
    outputFile.write("------------------------------------- \n")
    outputFile.write("Khan: " + str(khan) + "% (" + str(khanvotes) + ") \n")
    outputFile.write("Correy: " + str(correy) + "% (" + str(correyvotes) + ") \n")
    outputFile.write("Li: " + str(li) + "% (" + str(livotes) + ")")
    outputFile.write("O'Tooley: " + str(tool) + "% (" + str(tooleyvotes) + ") \n")
    if max(khan, correy, li, tool) == khan:
        outputFile.write("Winner: Khan")
    elif max(khan, correy, li, tool) == correy:
        outputFile.write("Winner: Correy")
    elif max(khan, correy, li, tool) == li:
        outputFile.write("Winner: Li")
    else:
        outputFile.write("Winner: O'Tooley")
    outputFile.close()
