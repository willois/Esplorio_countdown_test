from datetime import datetime
def main():
    d = input('Please input a date in YYYY-MM-DD format')
    e = input('Please input the event on such deadline')

    def deadline_countdown():
        if len(d) > 0:
            year, month, day = map(int, d.split('-'))
            deadline = datetime(year, month, day)
            days_till_deadline = deadline - datetime.today()
            if len(e) > 0:
                print('{} days until {}'.format(days_till_deadline.days, e))
            else:
                print('{} days until {}'.format(days_till_deadline.days, d))
        else:
            a = "12-25"
            b = "Christmas"
            month, day = map(int, a.split('-'))
            if datetime.now().month > month:
                year = datetime.now().year + 1
                deadline = datetime(year, month, day)
                days_till_deadline = deadline - datetime.today()
                print('{} days until {}'.format(days_till_deadline.days, b))
            else:
                year = datetime.now().year
                deadline = datetime(year, month, day)
                days_till_deadline = deadline - datetime.today()
                print('{} days until {}'.format(days_till_deadline.days, b))

    deadline_countdown()
main()


