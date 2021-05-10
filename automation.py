import datetime
import csv


def pay_calculator():
    print("Hourly Calculator\n")
    date_started = str(input('Please input the date started. Format yyyy-mm-dd : '))
    time_started = input('specify time (24 hrs)started in HH:MM format: ').split(":")
    date_ended = str(input('Please input the date ended. Format yyyy-mm-dd: '))
    time_ended = input('specify time (24 hrs) ended in HH:MM format: ').split(":")

    ts = (":").join(time_started)
    te = (":").join(time_ended)

    # calculations
    time_s = [int(i) for i in time_started]

    time_e = [int(i) for i in time_ended]

    a = 60 * time_s[0] + time_s[1]
    b = 60 * time_e[0] + time_e[1]

    ans = b - a
    hourly_pay = 5
    if ans > 0:
        val = ans / 60
        money_earned = val * hourly_pay

        print("the hourly money earned: US$", money_earned, "cedis")

        header = ['Date Started', 'Time Started', 'Date Ended', 'Time Ended', 'Amount Earned']
        data = [date_started, ts, date_ended, te, f'US${money_earned}']

        with open('C:/Users/joshs/PycharmProjects/automation/moneyEarned2.csv', 'w', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)

            f.close()

    else:
        print("hours cannot be less than zero")


pay_calculator()
