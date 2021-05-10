import datetime #importing the date and time package
import csv #importing the csv package

#creating a function called pay_calculator

def pay_calculator():
    print("Hourly Calculator\n")
    date_started = str(input('Please input the date started. Format yyyy-mm-dd : '))   #receiving date started work input from user 
    time_started = input('specify time (24 hrs)started in HH:MM format: ').split(":")   #receiving input on time started work from user. Spliting time to seperate the hour and minute 
    date_ended = str(input('Please input the date ended. Format yyyy-mm-dd: '))         #receiving date ended work input from user 
    time_ended = input('specify time (24 hrs) ended in HH:MM format: ').split(":")      #receiving input on time ended work from user. Spliting time to seperate the hour and minute 

    ts = (":").join(time_started)       #rewriting the time recieved into time format 
    te = (":").join(time_ended)

    # calculations
    time_s = [int(i) for i in time_started]     #looping through the string type time and changing them into integers

    time_e = [int(i) for i in time_ended]

    a = 60 * time_s[0] + time_s[1]              #converting the entire time into minutes.  
    b = 60 * time_e[0] + time_e[1]

    time_diff = b - a                       #obtaining the differencec in the timein minutes
    hourly_pay = 5                          #hourly wage is US$5
    if ans > 0:                             #setting an if condition that works for only when time is greater than 0.
        val = time_diff / 60                #the difference of time in minutes is converted to hours in float type
        money_earned = val * hourly_pay     #the wages recieved for period worked is calculated here 

        print("the hourly money earned: US$", money_earned)    #result or total wages earned for the period worked is printed. 

        header = ['Date Started', 'Time Started', 'Date Ended', 'Time Ended', 'Amount Earned']      #a header is created for the csv
        data = [date_started, ts, date_ended, te, f'US${money_earned}']                             #The data generated from the interaction with the user is collected

        with open('timetracker.csv', 'w', newline='', encoding='UTF8') as file:  #writing a csv file using the writer 
            writer = csv.writer(file)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)

    else:
        print("hours cannot be less than zero")


pay_calculator()
