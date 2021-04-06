import os
import csv

#create path
budget_data_csv = os.path.join ("..","pyBank", "resources2", "budget_data.csv")

#define variables 
Months_Amount = 0
Profit = 0
Months = []
Total_Profit = 0
Difference = 0
Total_Difference = []


#open the csv file budget data
with open(budget_data_csv)as csvfile:
    csv_reader=csv.reader(csvfile, delimiter= ",")

    csvheader=next(csv_reader)


     #creat a loop to read through data after header
    for row in csv_reader:
       
        #find the number of months 
        Months_Amount += 1


        #find the total profit 
        Total_Profit = Total_Profit + int(row[1])

        #month total     
        Months.append(str(row[0]))

        
        if Difference != 0:

            #initail porfit
            profit = int(row[1])

            #profit change
            Difference = profit -Difference

            #store change
            Total_Difference.append(Difference)

            Difference = int(row[1])

        elif Difference == 0:
            Difference = int(row[1])
    
    #no change month 1
    Months.pop(0)

        
    #find increase
    Greatest_Increase = Total_Difference.index(max(Total_Difference))
    Greatest_Decrease = Total_Difference.index(min(Total_Difference))

    #find months
    Increase_Difference = (Months[int(Greatest_Increase)], max(Total_Difference))
    Decrease_Difference = (Months[int(Greatest_Decrease)], min(Total_Difference))
    
    #find the average of total change 
    mean=sum(Total_Difference)/float(len(Total_Difference))  
    mean=round(mean,2)

    #print results 
    print(f'Financial Analysis')
    print(f'-------------------------------------------')
    print(f'Total Months: {Months_Amount}')
    print(f'Net Profit: {Total_Profit}')
    print(f'Average Monthly Change: {mean}')
    print(f'Greatest Increase in Profits: {Increase_Difference}')
    print(f'Greatest Loss In Profits: {Decrease_Difference}')
    
    #text path
    PyBanktxt =os.path.join('..','pyBank', 'PyBanktxt')

    #get text
    with open(PyBanktxt, 'w') as txtfile:
        txtfile.write('Financial Analysis')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Months: {Months_Amount}')
        txtfile.write(f'\nNet Profit: {Total_Profit}')
        txtfile.write(f'\nAverage Monthly Change: {mean}')
        txtfile.write(f'\nGreatest Increase In Profits: {Increase_Difference}')
        txtfile.write(f'\nGreatest Loss In Profits: {Decrease_Difference}')





    

    
    
      
